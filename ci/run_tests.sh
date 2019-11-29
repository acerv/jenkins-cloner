#!/bin/bash

# exit at first error
set -e

# create jenkins services
docker run --name jenkins1 -d -v $(pwd)/ci/jenkins1:/var/jenkins_home -p 8081:8080 -p 50001:50000 jenkins/jenkins:lts
docker run --name jenkins2 -d -v $(pwd)/ci/jenkins2:/var/jenkins_home -p 8082:8080 -p 50002:50000 jenkins/jenkins:lts

# show jenkins folders
ls -la ci/jenkins1
ls -la ci/jenkins2

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
