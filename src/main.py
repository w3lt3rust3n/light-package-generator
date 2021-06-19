#! /usr/bin/env python3
# coding: utf-8

#--------------------------------------------------------------------------------------------------------------
# LPG - Light Project Manager, a simple python program for lazy web developers ;)
# CAUTION : expect unexpected behaviors on Windows machines. May work as expected under GNU/Linux systems.
# Made with love by Maxence Buisson for the fun of it.
# 
# Contact : weltrusten@philentropy.org
# 
# Enjoy !
#---------------------------------------------------------------------------------------------------------------

import argparse
import generator.generator as pg
import depchecker.depcheck as dc
import preparator.preparator as pp

def show_info():
    from os import getenv; user = getenv("USER")
    print("\033[35m<Light Project Generator - version 0.0.2>\033[0m")
    print("\033[35mHello {}\033[0m".format(user))
    print("Supports the following technolgies: ")
    print("\tReactJS\n\tSymfony\n\tFlutter")
    print("\n")
    print("Running \033[32m'lpg --prepare flutter'\033[0m will try to automaticaly install flutter on your system.")
    print("Running \033[32m'lpg --checkdep symfony'\033[0m will check if you have all the requiered dependencies.")
    print("Running \033[32m'lpg --generate react /home/user/my-project-dir'\033[0m will generate the project at the given path.")
    print("If the directory doesn't exist, LPG will create it and ask for a project name.")

def parse_arguments():
    parser = argparse.ArgumentParser(prog='lpg', description='Light way to generate web projects using CLI')
    parser.add_argument('--checkdep', '-c', help='Check dep')
    parser.add_argument('--info', '-i', help='Show informations about LPG')
    parser.add_argument('--prepare', '-p', nargs=1, help='Prepare system with given technology')
    parser.add_argument('--generate', '-g', nargs=2, help='Generate a project with the given technology and path')

    return parser.parse_args()

def main():
    args = parse_arguments()
    print(args)
    if args.generate is None:
        pass
    else:
        if args.generate[0] == "react":
            lang = args.generate[0]
            path = args.generate[1]
            gp = pg.Generator(lang, path)
            gp.project_generator()
            
        elif args.generate[0] == "symfony":
            lang = args.generate[0]
            path = args.generate[1]
            gp = pg.Generator(lang, path)
            gp.project_generator()
            
        elif args.generate[0] == "flutter":
            lang = args.generate[0]
            path = args.generate[1]
            gp = pg.Generator(lang, path)
            gp.project_generator()
            
        else: 
            print("{} is not a valid technology, see --help".format(args.generate[0]))
    
    if args.info is None:
        pass
    else:
        show_info()
    
    if args.checkdep is None:
        pass
    else:
        if args.checkdep == "react" or args.checkdep == "flutter" or args.checkdep == "symfony":
            arg = args.checkdep
            print(arg)
        
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
            installer = pp.Preparator(arg)
            installer.init_preparator(arg)
        else:
            pass

if __name__ == "__main__":
    main()

    

