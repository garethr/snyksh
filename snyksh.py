#!/bin/env python3

"""
Snyk Shell provides a convenient shell interface to the Snyk API. You can
use any valid Python expression as well as make calls to the Snyk API using
the pre-configured Snyk API client. When you load the the shell it will
pre-load a list of your organizations and projects so you have some data to explore.
"""

import os
import sys

import prettyprinter
import snyk
from IPython.terminal.embed import InteractiveShellEmbed
from prettyprinter import cpprint as pprint
from termcolor import colored, cprint

prettyprinter.install_extras(include=["requests", "dataclasses"])


def run():
    try:
        token = os.environ["SNYK_TOKEN"]
    except KeyError:
        sys.exit("You must provide a SNYK_TOKEN to run Snyk Shell")
    client = snyk.SnykClient(token)
    organizations = client.organizations.all()
    projects = client.projects.all()

    shell = InteractiveShellEmbed(banner1=colored("Welcome to Snyk Shell", "blue"))

    shell(
        colored(
            "The following objects and methods are currently available:\n"
            "  client - An instance of the Snyk client, which can be used to make requests to the API\n"
            "  organizations - A prepopulated list of the Snyk organizations you are a member of\n"
            "  projects - A prepopulated list of all of your Snyk projects\n"
            "  pprint() - A pretty printer for objects returns by the API\n"
        )
    )


if __name__ == "__main__":
    run()
