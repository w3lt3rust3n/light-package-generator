#! /usr/bin/env python3
# coding: utf-8

#---------------------------------------------------------------------
# # LPG - Light Project Manager, a simple python program for lazy web
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
#---------------------------------------------------------------------

""" gngn """
import subprocess
import re
import logging as lg

from os import getenv
from os import path
from sh import ErrorReturnCode, which

import utils.utilities as util

lg.basicConfig(level=lg.DEBUG)

class Checker:
    """ gngn """
    LPG_DIR = ".lpg/"
    CHECK_DIR = ".lpg/check/"
    SCRIPTS_DIR = ".lpg/scripts"

    def __init__(self, lang=""):
        self.lang = lang
        self.checkd = self.CHECK_DIR
        self.home = getenv("HOME")
        self.homed = self.home + '/'

    def __check_php_version(self, dest):
        php_path = which("php")
        if php_path != "":
            try:
                check_dir = (self.homed + dest)
                if path.exists(check_dir):
                    check_file = check_dir + 'php-ver.data'
                    with open(check_file, 'w+') as check_output:
                        try:
                            subprocess.run([php_path, '-v'], stdout=check_output, check=True)
                        except subprocess.SubprocessError as error:
                            lg.error("Error : %s", error)
                    script_path = self.homed + self.SCRIPTS_DIR + '/'
                    script_file = script_path + "lpg-check-php.sh"

                    try:
                        output_file = check_dir + 'php-ver.tmp'
                        subprocess.run([script_file, check_file, output_file], check=True)

                        try:
                            with open(output_file, "r") as output:
                                str_ver = output.readline()
                            try:
                                ver = re.search(r'.\..\...', str_ver) # working here
                                if ver:
                                    found = ver.group()
                            except AttributeError as error:
                                ver = ''
                                lg.critical("%s", error)

                            if found < '7.2.5':
                                lg.warning("PHP is outdated")
                                util.print_no()
                            else:
                                util.print_yes()
                        except FileNotFoundError as error:
                            lg.critical("%s", error)
                    except subprocess.SubprocessError as error:
                        lg.critical("%s", error)
            except OSError as error:
                lg.critical("%s", error)

    @classmethod
    def check_composer(cls):
        """ gngngn """
        try:
            which("composer")
            util.print_yes()
        except ErrorReturnCode as error:
            lg.warning("%s", error)

    @classmethod
    def __check_react(cls):
        util.pcolor("NPM is installed : ", "yellow")
        try:
            which("npm")
            util.print_yes()
        except ErrorReturnCode as error:
            util.print_no()
            lg.warning("%s", error)

        util.pcolor("NPX is installed : ", "yellow")
        try:
            which("npx")
            util.print_yes()
        except ErrorReturnCode as error:
            util.print_no()
            lg.warning("%s", error)

    def __check_symfony(self):
        util.pcolor("PHP 7.2.5 or higher is installed : ", "yellow")
        try:
            self.__check_php_version(self.checkd)
        except ErrorReturnCode as error:
            lg.warning("%s", error)

        util.pcolor("Composer is installed : ", "yellow")
        try:
            self.check_composer()
        except ErrorReturnCode as error:
            lg.warning("%s", error)

        input("Press a key to launch dep analysis")
        try:
            arg = ['symfony', 'check:requirements']
            subprocess.run(arg, check=True)
        except subprocess.SubprocessError as error:
            lg.critical("%s", error)

    @classmethod
    def check_flutter(cls):
        """ gngngn """
        util.pcolor("Flutter is installed : ", "yellow")
        try:
            flutter_path = which("flutter")
            util.print_yes()
            input("Press a key to launch dep analysis")
            try:
                arg = [flutter_path, 'doctor']
                subprocess.run(arg, check=True)
            except subprocess.SubprocessError as error:
                lg.warning("%s", error)
            lg.info("Some packages might miss. Check output and try to run this command again")
        except ErrorReturnCode as error:
            lg.warning("%s", error)
            util.print_no()

    def __check_bundle(self):
        """ gngn """
        bundle = [
            'react',
            'symfony',
            'flutter'
        ]

        util.pcolor("Checking React, Symfony and Flutter", "bright_cyan")
        i = 0
        for item in bundle:
            #print(item)
            util.pcolor("Is {} installed ?".format(item), "cyan")
            if item == "react":
                self.__check_react()
            elif item == "symfony":
                self.__check_symfony()
            elif item == "flutter":
                self.check_flutter()
            else:
                raise ErrorReturnCode
            i += 1

    def init_checker(self):
        """ gngn """
        if self.lang == 'react':
            self.__check_react()
        elif self.lang == 'symfony':
            self.__check_symfony()
        elif self.lang == 'flutter':
            self.check_flutter()
        elif self.lang == 'all':
            self.__check_bundle()
        else:
            print("Hummm")
