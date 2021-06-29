#! /usr/bin/env python3
# coding: utf-8

"""gngng"""
import subprocess
import logging as lg
from os import path, getenv, mkdir
from sh import ErrorReturnCode, which
import depchecker.depcheck as dc

class Preparator:
    """gngngng"""
    LPG_DIR = "/.lpg/"
    CONFIG_DIR = "/.lpg/config"

    def __init__(self, lang):
        self.lang = lang
        self.util = dc.Checker(lang)

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
        self.util.pcolor("Done", "green")

    @classmethod
    def __edit_bashrc(cls):
        util = dc.Checker()
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
        util = dc.Checker()
        flutter_full_path = flutter_path + "/bin/flutter"
        arg = [flutter_full_path, "precache"]
        doctor = [flutter_full_path, "doctor"]

        util.pcolor("Precache in progress...", "yellow")
        try:
            subprocess.run(arg, check=True)
        except subprocess.SubprocessError as error:
            lg.critical("%s", error)
            raise error
        util.pcolor("Running doctor...", "yellow")
        try:
            subprocess.run(doctor, check=True)
        except subprocess.SubprocessError as error:
            lg.critical("%s", error)
            raise error
        return True
        
    def _get_flutter_src(self):
        home = getenv("HOME")
        self.util.pcolor("Download Flutter at ({} if left blank):".format(home), "cyan")
        flutter_git_path = input("@ ")
        if flutter_git_path == '':
            self.util.pcolor("Default path will be used to clone Flutter", "cyan")
            flutter_git_path = home
        if path.exists(flutter_git_path):
            self.util.pcolor("flutter will be cloned at {}".format(flutter_git_path), "cyan")
        else:
            try:
                mkdir(flutter_git_path)
            except ErrorReturnCode as error:
                raise error

            self.util.pcolor("flutter will be cloned at {}".format(flutter_git_path), "cyan")

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
        except subprocess.SubprocessError as error:
            lg.critical("%s", error)
            raise error
        return True

    def init_preparator(self, lang):
        """gngngn"""
        if lang == "flutter":
            self.util.pcolor("Is Git installed ?", "yellow")
            if self.is_git_installed() is True:
                self.util.print_yes()
            else:
                self.util.print_no()
            self.util.pcolor("--> Cloning Flutter stable git repository", "yellow")
            try:
                self._get_flutter_src()
                self.util.pcolor("Flutter source successfuly cloned", "green")
            except:
                self.util.pcolor("Something went wrong during cloning process.", "red")
            self.util.pcolor("--> Editing the bashrc", "yellow")
            try:
                self.__edit_bashrc()
                self.util.pcolor("Path is set", "green")
            except:
                self.util.pcolor("Something went wrong during path edit", "red")

            # if self._get_flutter_src() is True:
            #     self.util.pcolor("Flutter source successfuly cloned", "green")
            # else:
            #     self.util.pcolor("Something went wrong during cloning process.", "red")
            # if self.__edit_bashrc() is True:
            #     self.util.pcolor("Path is set", "green")
            # else:
            #     self.util.pcolor("Something went wrong during path edit", "red")
            # # if self.__init_flutter_precache() is True:
            # #     self.util.pcolor("Precache is done", "green")
            # # else:
            # #     self.util.pcolor("Something went wrong during precache", "red")
        elif lang == "react":
            pass
        elif lang == "symfony":
            pass
        elif lang == "all":
            pass
