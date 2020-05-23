import os
import subprocess

package_list = []


def add_package_to_install_list(package: str):
    # adds
    package_list.append(package)


def remove_package_from_install_list(package: str):
    if package in package_list:
        package_list.remove(package)


def install_package(package_list: list):
    for package in package_list:
        os.system("pip install {}".format(package))
        
def installed_packages():
    installed_packages = []
    exitcode, output = subprocess.getstatusoutput("pip freeze")
    for line in output.split('\n'):
        name, version = line.split('==')
        installed_packages.append([name, version])
    return installed_packages

def delete_packages(package_name: str):
    pass
