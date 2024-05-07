#!/usr/bin/python3
"""  Fabric script that creates and distributes
     an archive to your web servers """
from os.path import getsize
from fabric.api import *
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy
env.hosts = ['52.86.126.184', '18.207.142.29']


pack_path = do_pack()


def deploy():
    """ deploy the archive """
    if pack_path is None:
        return False
    print(f"web_static packed: {pack_path} -> "
          f"{getsize(pack_path)}Bytes")
    return do_deploy(pack_path)
