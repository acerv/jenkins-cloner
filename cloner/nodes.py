"""
.. module:: nodes
   :platform: Multiplatform
   :synopsis: nodes cloner implementation
   :license: GPLv2
.. moduleauthor:: Andrea Cervesato <andrea.cervesato@mailbox.org>
"""
import warnings
from cloner import show_status
from cloner import JenkinsCloner
from jenkinsapi.jenkins import Jenkins


class JenkinsNodesCloner(JenkinsCloner):
    """
    Cloner for jenkins nodes.
    """

    @show_status
    def _clone_node(self, server1, server2, node_name):
        """
        Clone a node from one server to an another server.
        """
        if node_name == "master":
            return

        node1 = server1.get_node(node_name)
        config = node1.get_config()

        node2 = None
        if not server2.has_node(node_name):
            node2 = server2.create_node(node_name)
        else:
            node2 = server2.get_node(node_name)

        node2.upload_config(config)

    @show_status
    def _clone_nodes(self, server1, server2):
        """
        Clone all nodes from server1 to server2.
        """
        cloned = list()
        not_cloned = list()

        for node_name in server1.nodes.keys():
            try:
                self._clone_node(server1, server2, node_name)
                cloned.append(node_name)
            except Exception as err:
                warnings.warn("WARNING: %s" % str(err))
                not_cloned.append((node_name, str(err)))

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

        return self._clone_nodes(server1, server2)
