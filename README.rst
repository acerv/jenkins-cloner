.. image:: https://travis-ci.org/acerv/jenkins-cloner.svg?branch=master
    :target: https://travis-ci.org/acerv/jenkins-cloner

Introduction
============

Jenkins cloner permits to clone:

* plugins
* slaves
* jobs

from one jenkins server to an another jenkins server.

Command line::

    Usage: jenkins-cloner [OPTIONS]

    Jenkins master cloner tool

    Options:
    -c, --config TEXT  configuration file
    -j, --jobs         clone jobs
    -p, --plugins      clone plugins
    -n, --nodes        clone nodes
    -d, --debug        debug mode
    --help             Show this message and exit.

Configuration
=============

Before using the application, a configuration file has to be defined.
Suppose we call it ``config.ini``::

    [server1]
    url = https://my.jenkins.server1.com/
    username = admin
    token = <admin_token>

    [server2]
    url = https://my.jenkins.server2.com/
    username = admin
    token = <admin_token>

Cloning
=======

To clone Jenkins server plugins into an another Jenkins server::

    jenkins-cloner -c config.ini -j

To clone Jenkins server nodes into an another Jenkins server::

    jenkins-cloner -c config.ini -n

To clone Jenkins server jobs into an another Jenkins server::

    jenkins-cloner -c config.ini -p

Installation
============

To install ``jenkins-cloner``, use virtualenv::

    cd jenkins-cloner
    virtualenv venv

    # on windows
    venv\Script\activate
    # on linux
    source venv/bin/activate

    python setup.py install

License
=======

This project has been developed under terms of the GPLv2 license.