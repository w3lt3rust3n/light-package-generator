#! /usr/bin/env python3
# coding: utf-8

#--------------------------------------------------------------------------------------------------------------
# LPG - Light Project Manager, a simple python program for lazy web developers ;)
#
# generator.py :
#
# CAUTION : expect unexpected behaviors on Windows machines. May work as expected under GNU/Linux systems.
#
# Made with love by Maxence Buisson for the fun of it.
# Contact : weltrusten@philentropy.org
#
# Enjoy !
#---------------------------------------------------------------------------------------------------------------

import os
from sh import mkdir
import subprocess

# \033[32m -> Green
# \033[31m -> Red
# \033[1;96m -> Bold - Bright Cyan
# \033[36m -> Cyan | \033[4;36m -> Underlined - Cyan

class Generator:
    SCRIPTS_DIR = ".lpg/scripts"

    def __init__(self, lang, path):
        self.lang = lang
        self.path = path

    def __launch_script(self):
        project_name = input("Set a project name : ")
        home = os.getenv("HOME")
        script_path = home + "/" + self.SCRIPTS_DIR + "/lpg-" + self.lang + "-init.sh"

        print("LPG will create the project {}".format(project_name))
        print("Location : {}".format(self.path))
        print("Type : {}".format(self.lang))

        while input("Confirm ? [y/n]") != 'y':
            return False

        try:
            subprocess.call([script_path, self.path, project_name])
        except subprocess.CalledProcessError:
            print("\033[31mError while executing script, no file !\033[0m")

    def project_generator(self):
        print("\033[36m--> Generating the project...\033[0m")
        if os.path.exists(self.path):
            Generator.__launch_script(self)
        else:
            print("\033[36m--> Creating project directory.\033[0m ")
            try:
                mkdir(self.path)
            except mkdir.ErrorReturnCode_2:
                print("\033[31mError while creating project directory\033[0m")

            if os.path.exists(self.path):
                print("\033[36m--> Launching script\033[0m")
                Generator.__launch_script(self)
            else:
                return False
