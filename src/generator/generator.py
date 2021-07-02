#! /usr/bin/env python3
# coding: utf-8

#------------------------------------------------------------------------------
# LPG - Light Projects Generator, a simple python package for lazy web
# developers ;)
#
# generator.py : All that LPG needs to generate project using args
# given by option -g
#
# CAUTION : expect unexpected behaviors on Windows machines. May work as
# expected under GNU/Linux systems.
#
# Made with love by Maxence Buisson for the fun of it.
# Contact : weltrusten@philentropy.org
#
# Enjoy !
#------------------------------------------------------------------------------

""" gngngn """
import os
import subprocess
import logging as lg

from os import mkdir

import utils.utilities as util

lg.basicConfig(level=lg.DEBUG)

class Generator:
    """ Generator is the class that contains features to generate
    web projects """
    SCRIPTS_DIR = ".lpg/scripts"

    def __init__(self, lang, path):
        self.lang = lang
        self.path = path
        self.home = os.getenv("HOME")

    def __launch_script(self):
        project_name = input("Set a project name : ")
        home = self.home
        script_path = [
            home + "/" + self.SCRIPTS_DIR + "/lpg-" + self.lang + "-init.sh",
            self.path,
            project_name
        ]
        util.pcolor("LPG will create the project {}".format(project_name), "cyan")
        util.pcolor("Location : {}".format(self.path), "cyan")
        util.pcolor("Type : {}".format(self.lang), "cyan")

        if input("Confirm ? [y/n]") != 'y':
            lg.info("Cancelling...")
        else:
            try:
                subprocess.run(script_path, check=True)
            except subprocess.SubprocessError as error:
                lg.critical("%s", error)

    def project_generator(self):
        """ Generate the given project """
        util.pcolor("--> Generating the project...", "cyan")
        if os.path.exists(self.path):
            Generator.__launch_script(self)
        else:
            util.pcolor("--> Creating project directory.", "cyan")
            try:
                mkdir(self.path)
            except OSError as error:
                lg.critical("%s", error)

            if os.path.exists(self.path):
                util.pcolor("--> Launching script", "cyan")
                Generator.__launch_script(self)
            else:
                lg.critical("%s", error)
                raise OSError
