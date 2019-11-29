"""
.. module:: jobs
   :platform: Multiplatform
   :synopsis: jobs cloner implementation
   :license: GPLv2
.. moduleauthor:: Andrea Cervesato <andrea.cervesato@mailbox.org>
"""
import warnings
from cloner import show_status
from cloner import JenkinsCloner
import jenkins


class JenkinsJobsCloner(JenkinsCloner):
    """
    Cloner for jenkins jobs.
    """

    @show_status
    def _clone_job(self, server1, server2, job_location):
        """
        Clone a job from one server to an another server.
        """
        config = server1.get_job_config(job_location)
        if server2.job_exists(job_location):
            server2.reconfig_job(job_location, config)
        else:
            server2.create_job(job_location, config)

    @show_status
    def _clone_jobs(self, server1, server2):
        """
        Clone all jobs from server1 to server2.
        """
        cloned = list()
        not_cloned = list()

        jobs = server1.get_all_jobs()
        for job in jobs:
            job_name = job['fullname']
            try:
                self._clone_job(server1, server2, job_name)
                cloned.append(job_name)
            except Exception as err:
                warnings.warn("WARNING: %s" % str(err))
                not_cloned.append((job_name, str(err)))

        return cloned, not_cloned

    def _create_server(self, config):
        """
        Create a Jenkins server object.
        """
        url = config["url"]
        username = config["username"]
        token = config["token"]

        server = jenkins.Jenkins(url, username, token)
        return server

    def clone(self, config):
        server1 = self._create_server(config["server1"])
        server2 = self._create_server(config["server2"])

        return self._clone_jobs(server1, server2)
