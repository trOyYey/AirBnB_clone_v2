#!/usr/bin/python3
"""fabric script that distributes an archive to a webserver"""
from os.path import exists
from fabric.api import *
env.hosts = ['52.86.126.184', '	18.207.142.29']


def do_deploy(archive_path):
    """ distributes an archive to a server
    Args:
        archive_path : file path
    Return:
        True for success and False for failing
    """
    if not exists(archive_path):
        return False
    serverP = archive_path.replace("versions", "/tmp")
    uploadF = put(archive_path, serverP)
    if uploadF.failed:
        return False
    fileN = serverP.split('/')[-1].split('.')[0]
    fileP = f"/data/web_static/releases/{fileN}"
    createF = sudo(f"mkdir -p {fileP}")
    if createF.failed:
        return False
    unpackF = sudo(f"tar -xzf {serverP} -C {fileP}")
    if unpackF.failed:
        return False
    removeF = sudo(f"rm {serverP}")
    if removeF.failed:
        return False
    serverP = fileP
    moveF = sudo(f"mv {serverP}/web_static/* /data/web_static/releases/{fileN}/")
    if moveF.failed:
        return False
    removeF2 = sudo(f"rm -rf {serverP}/web_static")
    if removeF2.failed:
        return False
    removeF3 = sudo("rm -rf /data/web_static/current")
    if removeF3.failed:
        return False
    symboF = sudo(f"ln -s {fileP}/ /data/web_static/current")
    if symboF.failed:
        return False
    print("New version deployed!")
    return True
