#!/bin/bash

# exit at first error
set -e

# install jenkins-clone
python setup.py install

# get jenkins passwords
server1_password=$(docker exec jenkins1 cat /var/jenkins_home/secrets/initialAdminPassword)
server2_password=$(docker exec jenkins2 cat /var/jenkins_home/secrets/initialAdminPassword)

# create config.ini
echo "
[server1]
url = https://localhost:8081/
username = admin
password = $server1_password

[server2]
url = https://localhost:8082/
username = admin
password = $server2_password
" > ci/config.ini

# clone jobs/check cloning
jenkins-clone -c ci/config.ini --jobs
test -e ci/jenkins2/jobs/job1
test -e ci/jenkins2/jobs/job2
test -e ci/jenkins2/jobs/job3
