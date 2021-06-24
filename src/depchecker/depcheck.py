""" gngn """
import subprocess
import re
import logging as lg
from os import getenv
from os import path
from sh import ErrorReturnCode, which

lg.basicConfig(level=lg.DEBUG)

class Checker:
    """ gngn """
    LPG_DIR = ".lpg/"
    CHECK_DIR = ".lpg/check/"
    SCRIPTS_DIR = ".lpg/scripts"

    def __init__(self, lang):
        self.lang = lang
        self.checkd = self.CHECK_DIR
        self.home = getenv("HOME")
        self.homed = self.home + '/'

    @classmethod
    def pcolor(cls, message, color):
        """gngngn"""
        if color == "yellow":
            return print("\033[33m{}\033[0m".format(message))
        if color == "bright_cyan":
            return print("\033[1;96m{}\033[0m".format(message))
        if color == "cyan":
            return print("\033[36m{}\033[0m".format(message))
        return None

    @classmethod
    def print_yes(cls):
        """gngngn"""
        return print("\033[32mYes\033[0m")

    @classmethod
    def print_no(cls):
        """gngngn"""
        return print("\033[31mNo\033[0m")

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
                                self.print_no()
                            else:
                                self.print_yes()
                        except FileNotFoundError as error:
                            lg.critical("%s", error)
                    except subprocess.SubprocessError as error:
                        lg.critical("%s", error)
            except OSError as error:
                lg.critical("%s", error)

    def __check_composer(self):
        try:
            which("composer")
            self.print_yes()
        except ErrorReturnCode as error:
            lg.warning("%s", error)

    def __check_react(self):
        self.pcolor("NPM is installed : ", "yellow")
        try:
            which("npm")
            self.print_yes()
        except ErrorReturnCode as error:
            self.print_no()
            lg.warning("%s", error)

        self.pcolor("NPX is installed : ", "yellow")
        try:
            which("npx")
            self.print_yes()
        except ErrorReturnCode as error:
            self.print_no()
            lg.warning("%s", error)

    def __check_symfony(self):
        self.pcolor("PHP 7.2.5 or higher is installed : ", "yellow")
        try:
            self.__check_php_version(self.checkd)
        except ErrorReturnCode as error:
            lg.warning("%s", error)

        self.pcolor("Composer is installed : ", "yellow")
        try:
            self.__check_composer()
        except ErrorReturnCode as error:
            lg.warning("%s", error)

        input("Press a key to launch dep analysis")
        try:
            arg = ['symfony', 'check:requirements']
            subprocess.run(arg, check=True)
        except subprocess.SubprocessError as error:
            lg.critical("%s", error)

    def __check_flutter(self):
        self.pcolor("Flutter is installed : ", "yellow")
        try:
            flutter_path = which("flutter")
            self.print_yes()
            input("Press a key to launch dep analysis")
            try:
                arg = [flutter_path, 'doctor']
                subprocess.run(arg, check=True)
            except subprocess.SubprocessError as error:
                lg.warning("%s", error)
            lg.info("Some packages might miss. Check output and try to run this command again")
        except ErrorReturnCode as error:
            lg.warning("%s", error)
            self.print_no()

    def __check_bundle(self):
        """ gngn """
        bundle = [
            'react',
            'symfony',
            'flutter'
        ]

        self.pcolor("Checking React, Symfony and Flutter", "bright_cyan")
        i = 0
        for item in bundle:
            #print(item)
            self.pcolor("Is {} installed ?".format(item), "cyan")
            if item == "react":
                self.__check_react()
            elif item == "symfony":
                self.__check_symfony()
            elif item == "flutter":
                self.__check_flutter()
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
            self.__check_flutter()
        elif self.lang == 'all':
            self.__check_bundle()
        else:
            print("HUmmm")
