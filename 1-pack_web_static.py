#!/usr/bin/python3
""" Fabric script that generates a .tgz archive of wb_static """
from os.path import isdir
from datetime import datetime
from fabric .api import *


def do_pack():
    """function that generates .tgz archive from web_static"""
    now = datetime.now()
    tf = f"{now.year}{now.month}{now.day}{now.hour}{now.minute}{now.second}"

    try:
        if not isdir("versions"):
            local("mkdir versions")
        print(f"Packing web_static to verwsions/web_static_{tf}.tgz")
        filep = f"versions/web_static_{tf}.tgz"
        scrpt = local(f"tar -cvzf {filep} web_static").succeeded
        if not scrpt:
            return None
        else:
            print(f"web_static packed: versions/web_static_{tf}.tgz")
            return (filep)
    except Exception as e:
        return None
