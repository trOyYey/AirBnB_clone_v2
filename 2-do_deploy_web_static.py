#!/usr/bin/python3
"""fabric script that distributes an archive to a webserver"""
from os.path import exists
from fabric.api import *
import os

env.hosts = ['52.86.126.184', '	18.207.142.29']
env.user = 'ubuntu'

def do_pack():
    """function that generates .tgz archive from web_static"""
    now = datetime.now()
    tf = f"{now.year}{now.month}{now.day}{now.hour}{now.minute}{now.second}"

    try:
        local("mkdir -p ./versions")
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


def do_deploy(archive_path):
    """ distributes an archive to a server
    Args:
        archive_path : file path
    Return:
        True for success and False for failing
    """
    if not os.path.exists(archive_path):
        return False
    file_name = archive_path.split('/')[1]
    file_path = '/data/web_static/releases/'
    releases_path = file_path + file_name[:-4]
    try:
        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(releases_path))
        run('tar -xzf /tmp/{} -C {}'.format(file_name, releases_path))
        run('rm /tmp/{}'.format(file_name))
        run('mv {}/web_static/* {}/'.format(releases_path, releases_path))
        run('rm -rf {}/web_static'.format(releases_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(releases_path))
        print('New version deployed!')
        return True
    except:
        return False
