#! /usr/bin/env python3
# coding: utf-8

#---------------------------------------------------------------------
# # LPG - Light Project Manager, a simple python program for lazy web
# developers ;)
#
# preparator.py : All that LPG needs to install required stuff 
# and dependencies. 
#
# CAUTION : expect unexpected behaviors on Windows machines.
# May work as expected under GNU/Linux systems.
#
# Made with love by Maxence Buisson for the fun of it.
# Contact : weltrusten@philentropy.org
#
# Enjoy !
#---------------------------------------------------------------------

"""gngng"""
import subprocess
import logging as lg
from os import path, getenv, mkdir
from sh import ErrorReturnCode, which
import utils.utilities as util

class Preparator:
    """gngngng"""
    LPG_DIR = "/.lpg/"
    CONFIG_DIR = "/.lpg/config"

    def __init__(self, lang):
        self.lang = lang
        
    @classmethod
    def __load_cfg(cls):
        home = getenv('HOME')
        conf_dir_path = home + '/'
        bashrc_file = ".bashrc"
        conf_file = conf_dir_path + bashrc_file
        arg = ["/usr/bin/bash", conf_file]

        if path.exists(conf_file):
            try:
                subprocess.run(arg, check=True)
            except subprocess.SubprocessError as error:
                lg.critical("%s", error)
                raise error
        else:
            raise FileExistsError
        return True

    @classmethod
    def is_git_installed(cls):
        """gngng"""
        try:
            which("git")
        except ErrorReturnCode as error:
            print("%s", error)
            raise error
        return True

    def __set_flutter_path(self, flutter_path):
        home = getenv('HOME')
        conf_dir = self.CONFIG_DIR
        conf_dir_path = home + conf_dir + '/'
        conf_file = conf_dir_path + "flutter.ini"

        content = 'export PATH="$PATH:' + flutter_path + '/bin"'

        with open(conf_file, 'w+') as cfg:
            cfg.write(content)
        util.pcolor("Done", "green")

    @classmethod
    def __edit_bashrc(cls):
        home = getenv('HOME')
        conf_dir_path = home + '/'
        bashrc_file = ".bashrc"
        conf_file = conf_dir_path + bashrc_file
        arg = ["/usr/bin/nano", conf_file]
        util.pcolor("Looking for bashrc", "yellow")
        if path.exists(conf_file):
            try:
                subprocess.run(arg, check=True)
                cls.__load_cfg()
            except subprocess.SubprocessError as error:
                lg.critical("%s", error)
                raise error
        else:
            raise FileExistsError
        return True

    @classmethod
    def __init_flutter_precache(cls, flutter_path):
        flutter_full_path = flutter_path + "/bin/flutter"
        arg = [flutter_full_path, "precache"]

        util.pcolor("Precache in progress...", "yellow")
        try:
            subprocess.run(arg, check=True)
        except subprocess.SubprocessError as error:
            lg.critical("%s", error)
            raise error
        return True
        
    @classmethod
    def __init_flutter_doctor(cls, flutter_path):
        flutter_full_path = flutter_path + "/bin/flutter"
        doctor = [flutter_full_path, "doctor"]

        util.pcolor("Running doctor...", "yellow")
        try:
            subprocess.run(doctor, check=True)
        except subprocess.SubprocessError as error:
            lg.critical("%s", error)
            raise error
        return True

    def _get_flutter_src(self):
        home = getenv("HOME")
        util.pcolor("Download Flutter at ({} if left blank):".format(home), "cyan")
        flutter_git_path = input("@ ")
        if flutter_git_path == '':
            util.pcolor("Default path will be used to clone Flutter", "cyan")
            flutter_git_path = home
        if path.exists(flutter_git_path):
            util.pcolor("flutter will be cloned at {}".format(flutter_git_path), "cyan")
        else:
            try:
                mkdir(flutter_git_path)
            except ErrorReturnCode as error:
                raise error

            util.pcolor("Flutter will be cloned at {}".format(flutter_git_path), "cyan")

        git_cmd_args = [
            'git', '-C', flutter_git_path, 'clone',
            'https://github.com/flutter/flutter.git',
            '-b', 'stable'
            ]

        try:
            subprocess.run(git_cmd_args, check=True)
            flutter_git_full_path = flutter_git_path + "/flutter"
            self.__set_flutter_path(flutter_git_full_path)
            self.__init_flutter_precache(flutter_git_full_path)
            self.__init_flutter_doctor(flutter_git_full_path)
        except subprocess.SubprocessError as error:
            lg.critical("%s", error)
            raise error
        return True

    def init_preparator(self, lang):
        """gngngn"""
        if lang == "flutter":
            util.pcolor("Is Git installed ?", "yellow")
            if self.is_git_installed() is True:
                util.print_yes()
            else:
                util.print_no()
            util.pcolor("--> Cloning Flutter stable git repository", "yellow")
            try:
                self._get_flutter_src()
                util.pcolor("Flutter source successfuly cloned", "green")
            except:
                util.pcolor("Something went wrong during cloning process.", "red")
            util.pcolor("--> Editing the bashrc", "yellow")
            try:
                self.__edit_bashrc()
                util.pcolor("Path is set", "green")
            except:
                util.pcolor("Something went wrong during path edit", "red")
        elif lang == "react":
            pass
        elif lang == "symfony":
            pass
        elif lang == "all":
            pass
