#! /usr/bin/env python3
# coding: utf-8

#--------------------------------------------------------------------------------------------------------------
# LPG - Light Project Manager, a simple python program for lazy web developers ;)
#
# main.py :
# Code to handle arguments and misc CLI features.
# 
# CAUTION : expect unexpected behaviors on Windows machines. May work as expected under GNU/Linux systems.
# 
# Made with love by Maxence Buisson for the fun of it.
# Contact : weltrusten@philentropy.org
# 
# Enjoy !
#---------------------------------------------------------------------------------------------------------------

import argparse
import generator.generator as pg
import depchecker.depcheck as dc
import preparator.preparator as pp

# \033[32m -> Green
# \033[31m -> Red
# \033[1;96m -> Bold - Bright Cyan
# \033[36m -> Cyan | \033[4;36m -> Underlined - Cyan

# show_info() :
# Just a function to display basic informations about how to use LPG.
# Setting up the username by getting the value from the env with getenv().
def show_info():
    from os import getenv; user = getenv("USER")
    print("<\033[1;96mLPG - version 0.0.2\033[0m>\n")
    print("Hello \033[36m{}\033[0m, thank you for using the \033[96mLight Package Generator\033[0m, the lazy".format(user))
    print("way to start web projects and install what you need if required dependencies are missing.\n")
    print("\033[4;36mSupports the following technologies:\033[0m")
    print("ReactJS\nSymfony\nFlutter\n")
    print("\033[4;36mBasic usage of LPG:\033[0m")
    print("Running \033[32mlpg --prepare flutter\033[0m will try to automaticaly install flutter on your system.")
    print("Running \033[32mlpg --checkdep symfony\033[0m will check if you have all that you need before to work.")
    print("Running \033[32mlpg --generate react /home/user/my-project-dir\033[0m will generate the project at the given path.\n")
    print("If the directory doesn't exist, LPG will create it and ask for a project name.\n")
    print("Use \033[32mlpg --help\033[0m or \033[32mlpg -h\033[0m for help")

def show_lpg_header(title):
    print("<\033[1;96mLight Project Generator -- {}\033[0m".format(title))


# parse_arguments() : 
# Just a function to define LPG's CLI arguments. 
# Instanciation of ArgumentParser and adding the different options before to return arguments
# when LPG will call the function from main().
def parse_arguments():
    parser = argparse.ArgumentParser(prog='lpg', description='Light way to generate web projects using CLI')
    parser.add_argument('--checkdep', '-c', help='Check dep', action='store_false')
    parser.add_argument('--info', '-i', help='Show informations about LPG', action='store_true')
    parser.add_argument('--prepare', '-p', nargs=1, help='Prepare system with given technology')
    parser.add_argument('--generate', '-g', nargs=2, help='Generate a project with the given technology and path')
    return parser.parse_args()

# main() :
# The function will parse the arguments by calling parse_arguments().
# We use if/elif/else statements in order to check what action to make from the given arguments.
# 
# if condition is None: is just a way to make it work, otherwise it fails. This part can be improved later
# but it works and do what we need to do: execute action given by arguments.
def main():
    args = parse_arguments()
    
    if args.generate is None:
       pass
    else:
        if args.generate[0] == "react":
            lang = args.generate[0]
            path = args.generate[1]
            show_lpg_header("React project")
            gp = pg.Generator(lang, path)
            gp.project_generator()
           
        elif args.generate[0] == "symfony":
            lang = args.generate[0]
            path = args.generate[1]
            show_lpg_header("Symfony project")
            gp = pg.Generator(lang, path)
            gp.project_generator()
            
        elif args.generate[0] == "flutter":
            lang = args.generate[0]
            path = args.generate[1]
            show_lpg_header("Flutter project")
            gp = pg.Generator(lang, path)
            gp.project_generator()
            
        else: 
            print("{} is not a valid technology, see --help".format(args.generate[0]))
    
    if args.info is None:
        pass
    else:
        show_info()
    
    if args.checkdep == "react" or args.checkdep == "flutter" or args.checkdep == "symfony":
            arg = args.checkdep
            print(arg)
            show_lpg_header("Check ReactJS")
            checker = dc.Checker(arg)
            checker.init_checker(arg)
    else: 
        print("{} is not a valid technology, see --help or --info".format(args.checkdep))
    
    if args.checkdep is None:
        pass
    else:
        if args.checkdep == "react" or args.checkdep == "flutter" or args.checkdep == "symfony":
            arg = args.checkdep
            print(arg)
            show_lpg_header("Check ReactJS")
            checker = dc.Checker(arg)
            checker.init_checker(arg)
        else: 
            print("{} is not a valid technology, see --help or --info".format(args.checkdep))
    if args.prepare is None:
        pass
    else:
        if args.prepare:
            arg = args.prepare
            print(arg)
            show_lpg_header("React project generator")
            installer = pp.Preparator(arg)
            installer.init_preparator(arg)
        else:
            pass

if __name__ == "__main__":
    main()

    

