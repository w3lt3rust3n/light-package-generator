#! /usr/bin/env python3
# coding: utf-8

#---------------------------------------------------------------------
# # LPG - Light Project Manager, a simple python program for lazy web
# developers ;)
#
# generator.py : All that LPG needs to generate project using args
# given by option -g
#
# CAUTION : expect unexpected behaviors on Windows machines.
# May work as expected under GNU/Linux systems.
#
# Made with love by Maxence Buisson for the fun of it.
# Contact : weltrusten@philentropy.org
#
# Enjoy !
#---------------------------------------------------------------------

""" gngngn """
import os
import subprocess
import logging as lg

from sh import mkdir

import utils.utilities as util

lg.basicConfig(level=lg.DEBUG)

class Generator:
    """ gngngn """
    SCRIPTS_DIR = ".lpg/scripts"

    def __init__(self, lang, path):
        self.lang = lang
        self.path = path

    def __launch_script(self):
        project_name = input("Set a project name : ")
        home = os.getenv("HOME")
        script_path = home + "/" + self.SCRIPTS_DIR + "/lpg-" + self.lang + "-init.sh"

        util.pcolor("LPG will create the project {}".format(project_name), "cyan")
        util.pcolor("Location : {}".format(self.path), "cyan")
        util.pcolor("Type : {}".format(self.lang), "cyan")

        while input("Confirm ? [y/n]") != 'y':
            return False

        try:
            subprocess.run(script_path, self.path, project_name, check=True)
        except subprocess.SubprocessError as error:
            lg.critical("Error while executing script, no file !", "red")

    def project_generator(self):
        """ gngngn """
        util.pcolor("--> Generating the project...", "cyan")
        if os.path.exists(self.path):
            Generator.__launch_script(self)
        else:
            util.pcolor("--> Creating project directory.", "cyan")
            try:
                mkdir(self.path)
            except mkdir.ErrorReturnCode_2:
                util.pcolor("Error while creating project directory", "red")

            if os.path.exists(self.path):
                util.pcolor("--> Launching script", "cyan")
                Generator.__launch_script(self)
            else:
                raise OSError
