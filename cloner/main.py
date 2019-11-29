"""
.. module:: main
   :platform: Multiplatform
   :synopsis: command main implementation
   :license: GPLv2
.. moduleauthor:: Andrea Cervesato <andrea.cervesato@mailbox.org>
"""
import click
import traceback
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import SafeConfigParser as ConfigParser
import cloner
from cloner.jobs import JenkinsJobsCloner
from cloner.nodes import JenkinsNodesCloner
from cloner.plugins import JenkinsPluginsCloner


def read_config(path):
    """
    Read the configuration file.
    """
    config = ConfigParser()
    config.read(path)
    return config


def validate_config(config, section):
    """
    Validate a configuration section.
    """
    if section not in config:
        raise ValueError("%s section is not defined\n" % section)

    section_cfg = config[section]
    for cfg in ["url", "username", "token"]:
        if cfg not in section_cfg:
            raise ValueError(
                "%s is not defined in section %s\n" %
                (cfg, section))
        elif not section_cfg[cfg]:
            raise ValueError(
                "%s is empty in section %s\n" %
                (cfg, section))


@click.command()
@click.option("-c", "--config", default="config.ini", help="configuration file")
@click.option("-j", "--jobs", is_flag=True, default=False, help="clone jobs")
@click.option("-p", "--plugins", is_flag=True, default=False, help="clone plugins")
@click.option("-n", "--nodes", is_flag=True, default=False, help="clone nodes")
@click.option("-d", "--debug", is_flag=True, default=False, help="debug mode")
def client(config, jobs, plugins, nodes, debug):
    """
    Jenkins master cloner tool
    """
    cloner.set_stdout_callback(click.echo)

    tool = None
    if plugins:
        tool = JenkinsPluginsCloner()
    if jobs:
        tool = JenkinsJobsCloner()
    if nodes:
        tool = JenkinsNodesCloner()

    if not tool:
        return

    try:
        configini = read_config(config)

        validate_config(configini, "server1")
        validate_config(configini, "server2")

        cloned, not_cloned = tool.clone(configini)

        if cloned:
            click.echo()
            click.secho("Cloned correctly:\n", fg="green")
            for clone in cloned:
                click.secho("    %s" % clone, fg="green")

        if not_cloned:
            click.echo()
            click.secho("Cloned failed:\n", fg="red")
            for not_clone in not_cloned:
                click.secho("    %s: %s" % (not_clone), fg="red")

    except Exception as err:
        click.secho("ERROR: %s\n" % str(err), fg="red", err=True)
        if debug:
            click.secho("\n%s\n" % traceback.format_exc(), fg="red", err=True)
