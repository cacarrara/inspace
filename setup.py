#!/usr/bin/env python
from setuptools import setup, find_packages


def get_requirements():
    requirements = []

    with open('requirements.txt', 'r') as req_file:
        for requirement in req_file:
            if requirement.startswith('#'):
                continue
            requirements.append(requirement.strip())

    return requirements


setup(
    name='inspace',
    version='0.0.1',
    url='https://github.com/cacarrara/inspace',
    description='Community knowledge register, organization and sharing.',
    long_description=open('README.md').read(),
    author='Caio Carrara',
    author_email='eu@caiocarrara.com.br',
    install_requires=get_requirements(),
    packages=find_packages(),
    include_package_data=True,
    license='GPL-3.0',
)
