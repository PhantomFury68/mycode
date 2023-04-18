#!/usr/bin/env python3


# import additional code
import shutil
import os

def main():
    """code to move files around"""
    # move into the working directory
    os.chdir('/home/student/mycode/')

    # copy the fileA to fileB
    shutil.move('raynor.obj', 'ceph_storage/')

    xname = input('What is the new name for kerrigan.obj? ')

    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

if __name__ == "__main__":
    main()
