"""
.. module:: plugins
   :platform: Multiplatform
   :synopsis: plugins cloner implementation
   :license: GPLv2
.. moduleauthor:: Andrea Cervesato <andrea.cervesato@mailbox.org>
"""
import warnings
from cloner import show_status
from cloner import JenkinsCloner
from jenkinsapi.jenkins import Jenkins


class JenkinsPluginsCloner(JenkinsCloner):
    """
    Cloner for jenkins plugins.
    """

    @show_status
    def _clone_plugin(self, server1, server2, plugin):
        """
        Clone a plugin from one server to an another server.
        """
        version = server1.plugins[plugin].version
        toinstall = "%s@%s" % (plugin, version)
        server2.install_plugin(toinstall, restart=True)

    @show_status
    def _clone_plugins(self, server1, server2):
        """
        Clone all plugins from one server to an another server.
        """
        cloned = list()
        not_cloned = list()

        for plugin in server1.plugins.keys():
            try:
                self._clone_plugin(server1, server2, plugin)
                cloned.append(plugin)
            except Exception as err:
                warnings.warn("WARNING: %s" % str(err))
                not_cloned.append((plugin, str(err)))

        return cloned, not_cloned

    def _server_login(self, config):
        """
        Create a Jenkins server object.
        """
        url = config["url"]
        username = config["username"]
        token = config["token"]

        server = Jenkins(url, username=username, password=token, lazy=True)
        return server

    def clone(self, config):
        server1 = self._server_login(config["server1"])
        server2 = self._server_login(config["server2"])

        return self._clone_plugins(server1, server2)
