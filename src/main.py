#! /usr/bin/env python3
# coding: utf-8

#------------------------------------------------------------------------------
# LPG - Light Project Manager, a simple python program for lazy web
# developers ;)
#
# main.py :
# Code to handle arguments and misc CLI features.
#
# CAUTION : expect unexpected behaviors on Windows machines. May work as
# expected under GNU/Linux systems.
#
# Made with love by Maxence Buisson for the fun of it.
# Contact : weltrusten@philentropy.org
#
# Enjoy !
#------------------------------------------------------------------------------

"""Importing argparse to work with CLI arguments."""
import argparse
from os import getenv

import generator.generator as pg
import depchecker.depcheck as dc
import preparator.preparator as pp

# Just a function to display basic informations about how to use LPG.
# Setting up the username by getting the value from the env with getenv().
def show_info():
    # \033[31m -> Red
    # \033[32m -> Green
    # \033[1;96m -> Bold - Bright Cyan
    # \033[36m -> Cyan | \033[4;36m -> Underlined - Cyan
    """Getting the username from environment variables"""
    user = getenv("USER")
    print("<\033[1;96mLPG - version 0.0.2\033[0m>\n")
    print("Hello \033[36m{}\033[0m, thank you for using the \033[96mLPG\
\033[0m, the lazy".format(user))
    print("way to start web projects and install what you need if required \
dependencies are missing.\n")
    print("\033[4;36mSupports the following technologies:\033[0m")
    print("ReactJS\nSymfony\nFlutter\n")
    print("\033[4;36mBasic usage of LPG:\033[0m")
    print("Running \033[32mlpg --prepare flutter\033[0m will try to\
automaticaly install flutter on your system.")
    print("Running \033[32mlpg --checkdep symfony\033[0m will check if you\
have all that you need before to work.")
    print("Running \033[32mlpg --generate react /home/user/my-project-dir\
    \033[0m will generate the project at the given path.\n")
    print("If the directory doesn't exist, LPG will create it and ask for a\
project name.\n")
    print("Use \033[32mlpg --help\033[0m or \033[32mlpg -h\033[0m for help")

def show_lpg_header(title):
    """show_lpg_header() : Just a dumb header to print."""
    return print("<\033[1;96mLight Project Generator -- {}\033[0m".format(title))

def parse_arguments():
    """Setting up the support of CLI arguments"""
    parser = argparse.ArgumentParser(prog='lpg', description='Light way to \
generate web projects using CLI')
    parser.add_argument('--checkdep', '-c', help='Check dep')
    parser.add_argument('--info', '-i', help='Show informations about LPG', action='store_true')
    parser.add_argument('--prepare', '-p', nargs=1, help='Prepare system with \
given technology')
    parser.add_argument('--generate', '-g', nargs=2, help='Generate a project \
with the given technology and path')
    return parser.parse_args()

def parse_prep_args(arg):
    """Checking arg for header"""
    if arg == "react":
        show_lpg_header("Installing React")
        installer = pp.Preparator(arg)
        installer.init_preparator(arg)
    if arg == "symfony":
        show_lpg_header("Installing Symfony")
        installer = pp.Preparator(arg)
        installer.init_preparator(arg)
    if arg == "flutter":
        show_lpg_header("Installing Flutter")
        installer = pp.Preparator(arg)
        installer.init_preparator(arg)
    if arg == "all":
        show_lpg_header("Installing the bundle")
        installer = pp.Preparator(arg)
        installer.init_preparator(arg)
    else :
        print("{} is not a valid technology to intall\
, see --help.".format(arg))

def parse_check_args(arg):
    """Checking arg for header"""
    if arg == "react":
        show_lpg_header("Check ReactJS")
        checker = dc.Checker(arg)
        checker.init_checker()
    elif arg == "flutter":
        show_lpg_header("Check Flutter")
        checker = dc.Checker(arg)
        checker.init_checker()
    elif arg == "symfony":
        show_lpg_header("Check Symfony")
        checker = dc.Checker(arg)
        checker.init_checker()
    elif arg == "all":
        show_lpg_header("Check for ReactJS, Flutter and Symfony")
        checker = dc.Checker(arg)
        checker.init_checker()
    else:
        print("{} is not a valid technology, see --help or --info".format(arg))

def parse_gen_args(arg):
    """Checking arguments for header and generator"""
    if arg == "react":
        lang = arg[0]
        path = arg[1]
        show_lpg_header("Generate React project")
        generate_project = pg.Generator(lang, path)
        generate_project.project_generator()
    elif arg == "symfony":
        lang = arg[0]
        path = arg[1]
        show_lpg_header("Generate Symfony project")
        generate_project = pg.Generator(lang, path)
        generate_project.project_generator()
    elif arg == "flutter":
        lang = arg[0]
        path = arg[1]
        show_lpg_header("Generate Flutter project")
        generate_project = pg.Generator(lang, path)
        generate_project.project_generator()
    else:
        print("{} is not a valid technology, see --help".format(arg))

# We use if/elif/else statements in order to check what action to make from the given arguments.
#
# If condition is None: is just a way to make it work, otherwise it fails.
# This part can be improved later but it works and do what we need to do:
# execute action given by arguments.
def main():
    """Parsing given arguments"""
    args = parse_arguments()
    if args.checkdep:
        arg = args.checkdep
        parse_check_args(arg)
    elif args.info:
        show_info()
    elif args.prepare:
        arg = args.prepare
        parse_prep_args(arg)
    elif args.generate:
        arg = args.generate
        parse_gen_args(arg)
    else:
        print("Invalid argument, see --help")

if __name__ == "__main__":
    main()
