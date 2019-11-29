"""
.. module:: setup
   :platform: Multiplatform
   :synopsis: Application installer
   :license: GPLv2
.. moduleauthor:: Andrea Cervesato <andrea.cervesato@mailbox.org>
"""

from setuptools import setup, find_packages

setup(
    name='jenkins-cloner',
    version='1.0',
    description='Jenkins Master Cloner',
    author='Andrea Cervesato',
    author_email='andrea.cervesato@mailbox.org',
    url="https://github.com/acerv",
    long_description=open('README.rst').read(),
    license="GPLv2",
    platforms=["linux", "windows"],
    python_requires=">=2.7.15, <=3.8.0",
    classifiers=[
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Utilities",
    ],
    packages=find_packages(),
    install_requires=[
        'click',
        'colorama',
        'jenkinsapi',
        'python-jenkins',
    ],
    entry_points={
        'console_scripts': [
            'jenkins-cloner=cloner.main:client',
        ],
    },
)
