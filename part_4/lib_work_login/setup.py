#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This module sets up the package for the lib_work_login"""

from setuptools import find_packages, setup

#with open("README.md", "r", encoding="utf-8") as fh:
#    long_description = fh.read()

setup(    
    name="lib_work_login",
    author="Justin Furuness",
    author_email="jfuruness@gmail.com",
    maintainer="Justin Furuness",
    maintainer_email="jfuruness@gmail.com",
    version="0.1.2",
    url="https://github.com/jfuruness/lib_work_login.git",
    download_url='https://github.com/jfuruness/lib_work_login.git',
    keywords=['Furuness', 'Login', 'login', 'terminal'],
    license="BSD",
    description="Logs you into work",
    #long_description=long_description,
    #long_description_content_type="text/markdown",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    python_requires=">=3.6",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pynput',
        'pytest',
    ],
    classifiers=[
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3'],
    entry_points={
        'console_scripts': [
            'login = lib_work_login.__main__:main',
            'configure = lib_work_login.__main__:configure',
        ]},
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
