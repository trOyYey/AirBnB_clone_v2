#!/usr/bin/python3
""" clean_up old versions or specified ones"""
from fabric.api import *
from os import listdir
env.hosts = ['54.209.125.126', '54.85.96.138']


def do_clean(number=0):
    """clean the files from oldest to newest

    Args:
        number: number from the oldest versions to clean
    """
    number = 1 if int(number) == 0 else int(number)
    fileL = sorted(listdir("versions"))
    for i in range(number):
        fileL.pop()
    for y in fileL:
        local(f"rm ./versions/{y}")

    with cd("/data/web_static/releases"):
        tempL = run("ls -tr").split()
        fileL = []
        for i in tempL:
            if "test" != i:
                fileL.append(i)
        for y in range(number):
            fileL.pop()
        for i in fileL:
            run(f"rm -rf ./{i}")
