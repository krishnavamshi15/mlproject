from setuptools import find_packages,setup
from typing import List

hypen_e_dot = '-e .'


def get_requriments(filename:str)->List[str]:
    with open(filename) as f:
        requriments = f.readlines()
        requriments = [req.replace('\n','') for req in requriments]
        
        
        if hypen_e_dot in requriments:
            requriments.remove(hypen_e_dot)
            
    return requriments

setup(
    name = 'mlproject',
    version='0.0.1',
    author='Krishna Vamshi',
    author_email='kvamshi2k2@gmail.com',
    packages=find_packages(),
    install_requires=get_requriments("requriments.txt")
)