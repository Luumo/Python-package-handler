import os
import subprocess

package_list = []


def add_package(package: str):
    package_list.append(package)


def remove_package(package: str):
    if package in package_list:
        package_list.remove(package)


def install_package(package_list: list):
    for package in package_list:
        #install all packages, call os.system() 
        #pip install all libraries
        os.system("pip install {}".format(package))
        
def installed_packages():
    exitcode, output = subprocess.getstatusoutput("pip freeze")
    print(output)