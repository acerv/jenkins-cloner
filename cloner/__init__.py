"""
.. module:: __init__
   : platform: Multiplatform
   : synopsis: Package initialization
   :license: GPLv2
.. moduleauthor:: Andrea Cervesato <andrea.cervesato@mailbox.org>
"""
import jenkins
import jenkinsapi

print_msg = None


def set_stdout_callback(stdout_callback):
    """
    Set the stdout callback.
    """
    global print_msg
    print_msg = stdout_callback


def show_status(func):
    """
    Decorator to wrap functions and provide a mechanism for stdout reports.
    """
    def wrapper(*args, **kwargs):
        if not print_msg:
            return

        arg_names = list()
        for arg in args:
            if isinstance(arg, jenkins.Jenkins):
                arg_names.append(arg.server)
            elif isinstance(arg, jenkinsapi.jenkins.Jenkins):
                arg_names.append(arg.base_server_url())
            elif isinstance(arg, JenkinsCloner):
                continue
            else:
                arg_names.append(str(arg))

        func_msg = "%s %r" % (func.__name__, arg_names)

        print_msg("-> %s" % func_msg)
        return func(*args, **kwargs)

    return wrapper


class JenkinsCloner:
    """
    Base classe for a jenkins data cloner.
    """

    def clone(self, config):
        """
        Clone jenkins data from one server to another.
        :param config: cloner configuration
        :type config: dict
        :return: tuple defined as following:

            (
                list(),      # cloned jobs
                list(tuple)  # not cloned jobs as (<job location>, <error>)
            )

        """
        raise NotImplementedError()
