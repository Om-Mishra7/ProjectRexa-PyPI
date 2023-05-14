from distutils.core import setup
from setuptools import find_packages
import os

# Optional project description in README.md:
current_directory = os.path.dirname(os.path.abspath(__file__))

try:
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''
setup(

# Project name: 
name='projectrexa',

# Packages to include in the distribution: 
packages=find_packages(','),

# Project version number:
version='0.0.0.4',

# List a license for the project, eg. MIT License
license='MIT',

# Short description of your library: 
description='A library to make it easier to use ProjectRexa SSO.',

# Long description of your library: 
long_description=long_description,
long_description_content_type='text/markdown',

# Your name: 
author='ProjectRexa',

# Your email address:
author_email='admin@projectrexa.ml',

# Link to your github repository or website: 
url='https://projectrexa.ml',

# Download Link from where the project can be downloaded from:
download_url='https://github.com/Om-Mishra7/ProjectRexa-PyPI/archive/refs/tags/v_0.0.0.4.tar.gz',

# List of keywords: 
keywords=['ProjectRexa'],

# List project dependencies: 
install_requires=['flask','cryptography','requests'],

# https://pypi.org/classifiers/ 
classifiers=['Development Status :: 2 - Pre-Alpha']
)