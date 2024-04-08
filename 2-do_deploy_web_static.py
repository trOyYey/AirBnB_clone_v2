#!/usr/bin/python3
"""fabric script that distributes an archive to a webserver"""
from os.path import exists
from fabric.api import *
env.hosts = ['54.209.125.126', '54.85.96.138']


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
    createF = run(f"mkdir -p {fileP}")
    if createF.failed:
        return False
    unpackF = run(f"tar -xzf {serverP} -C {fileP}")
    if unpackF.failed:
        return False
    removeF = run(f"rm {serverP}")
    if removeF.failed:
        return False
    serverP = fileP
    moveF = run(f"mv {serverP}/web_static/* /data/web_static/releases/{fileN}/")
    if moveF.failed:
        return False
    removeF2 = run(f"rm -rf {serverP}/web_static")
    if removeF2.failed:
        return False
    removeF3 = run("rm -rf /data/web_static/current")
    if removeF3.failed:
        return False
    symboF = run(f"ln -s {fileP}/ /data/web_static/current")
    if symboF.failed:
        return False
    print("New version deployed!")
    return True
