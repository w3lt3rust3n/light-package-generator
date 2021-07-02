#! /usr/bin/env python3
# coding: utf-8

#------------------------------------------------------------------------------
# LPG - Light Projects Generator, a simple python package for lazy web
# developers ;)
#
# depcheck.py : All that LPG needs to check system for the presence
# of required stuff and dependencies.
#
# CAUTION : expect unexpected behaviors on Windows machines.
# May work as expected under GNU/Linux systems.
#
# Made with love by Maxence Buisson for the fun of it.
# Contact : weltrusten@philentropy.org
#
# Enjoy !
#------------------------------------------------------------------------------

""" Importing required libs and modules """
import subprocess
import sys
import logging as lg

from os import getenv, path
from sh import ErrorReturnCode, which


import utils.utilities as util

lg.basicConfig(level=lg.DEBUG)

class Checker:
    """ Checker class contains all the features to check your system for React,
    Symfony and Flutter """
    CHECK_DIR = ".lpg/check/"
    SCRIPTS_DIR = ".lpg/scripts"

    def __init__(self, lang=""):
        self.lang = lang
        self.checkd = self.CHECK_DIR
        self.home = getenv("HOME")
        self.homed = self.home + '/'

    @classmethod
    def __check_composer(cls):
        """ Verify if Composer is installed on the system """
        composer_bin_path = which("composer")
        if composer_bin_path is None:
            lg.critical("Can't get Composer binary path. Please report the issue (see -i)")
            sys.exit()
        else:
            if path.exists(composer_bin_path):
                util.print_yes()
            else:
                util.print_no()
                lg.warning("Composer is not installed")

    @classmethod
    def check_react(cls):
        """ React projects need NPM and NPX in order to be generated """
        util.pcolor("Is NPM installed ?", "yellow")
        npm_bin_path = which("npm")
        if npm_bin_path is None:
            lg.critical("Can't get npm binary path. Please report the issue (see -i)")
            sys.exit()
        else:
            if path.exists(npm_bin_path):
                util.print_yes()
            else:
                util.print_no()
                lg.warning("npm is not installed")

        util.pcolor("Is NPX installed ?", "yellow")
        npx_bin_path = which("npx")
        if npx_bin_path is None:
            lg.critical("Can't get npx binary path. Please report the issue (see -i)")
            sys.exit()
        else:
            if path.exists(npx_bin_path):
                util.print_yes()
            else:
                util.print_no()
                lg.warning("npx is not installed")

    def check_symfony(self):
        """ Symfony projects need Composer in order to be generated """
        util.pcolor("Is Composer installed : ", "yellow")
        try:
            self.__check_composer()
        except ErrorReturnCode as error:
            util.print_no()
            lg.warning("%s", error)

        input("Press a key to launch dep analysis")
        try:
            arg = ['symfony', 'check:requirements']
            subprocess.run(arg, check=True)
        except subprocess.SubprocessError as error:
            lg.critical("%s", error)

    @classmethod
    def check_flutter(cls):
        """ Verify if Flutter is installed on the system """
        util.pcolor("Is Flutter installed ?", "yellow")
        flutter_bin_path = which("flutter")
        if flutter_bin_path is None:
            lg.critical("Can't get Flutter binary path. Please report the issue (see -i)")
            sys.exit()
        else:
            if path.exists(flutter_bin_path):
                util.print_yes()
            else:
                util.print_no()
                lg.warning("Flutter is not installed")

        input("Press a key to launch dep analysis")
        arg = [flutter_bin_path, 'doctor']

        try:
            subprocess.run(arg, check=True)
        except subprocess.SubprocessError as error:
            lg.warning("%s", error)

        lg.info("Some packages might miss. Check output and try to run this command again")

    def check_bundle(self):
        """ Verify if React, Symfony and Flutter are installed on the system """
        bundle = [
            'react',
            'symfony',
            'flutter'
        ]

        util.pcolor("Checking React, Symfony and Flutter", "bright_cyan")
        i = 0
        for item in bundle:
            util.pcolor("Is {} installed ?".format(item), "cyan")
            if item == "react":
                self.check_react()
            elif item == "symfony":
                self.check_symfony()
            elif item == "flutter":
                self.check_flutter()
            else:
                raise ErrorReturnCode
            i += 1

    def init_checker(self):
        """ Initiate and execute requested tasks to check the system """
        if self.lang == 'react':
            self.check_react()
        elif self.lang == 'symfony':
            self.check_symfony()
        elif self.lang == 'flutter':
            self.check_flutter()
        elif self.lang == 'all':
            self.check_bundle()
        # else:
        #     print("Hummm")
