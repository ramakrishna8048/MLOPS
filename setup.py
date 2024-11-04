from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->list[str]:     # this line we have defined a function whcih takes file path as str input and return type list of strings
    '''
    this function will return the list of requirements 
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]
    return requirements



setup(
name='mlops',
version='0.1',
author='rkreddy',
author_email='ramakrishnareddy731@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)