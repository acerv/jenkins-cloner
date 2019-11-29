
Introduction
============

Jenkins cloner permits to clone:

* plugins
* slaves
* jobs

All can be cloned from one jenkins server to an another jenkins server.

Installation
============

To install ``jenkins-cloner``, use virtualenv:

    cd jenkins-cloner
    virtualenv venv

    # on windows
    venv\Script\activate
    # on linux
    source venv/bin/activate

    python setup.py install

Configuration
=============

Before using the application, a configuration file has to be defined.
Suppose we call it ``config.ini``:

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

To clone Jenkins server plugins into an another Jenkins server:

    jenkins-cloner -c config.ini -j

To clone Jenkins server slaves into an another Jenkins server:

    jenkins-cloner -c config.ini -s

To clone Jenkins server jobs into an another Jenkins server:

    jenkins-cloner -c config.ini -p

License
=======

This project has been developed under terms of the GPLv2 license.