"""
Author: Eric Zair
File: dev_install.py
Date: 02/11/2019

All this does is install python libs needed to run this program in a jupyter
notebook.
"""
import subprocess
from os.path import exists


def main():
    if not exists('deps/requirements.txt'):
        print("Error, missing requirements.txt")
    else:
        print("Installing requirements for this project:")
        subprocess.call(['pip', 'install', '-r', 'deps/requirements.txt'])


if __name__ == '__main__':
    main()
