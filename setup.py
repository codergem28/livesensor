from setuptools import find_packages ,setup
from typing import List


def get_requirements()->list[str]:

    requirements_list = list[str] = []

    return requirements_list

setup(

    name= 'sensor',
    version="0.0.1",
    author="sudhanshu",
    author_email="sudhanshumtripathi28@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)