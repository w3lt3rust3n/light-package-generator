#! /usr/bin/env python3
# coding: utf-8

#------------------------------------------------------------------------------
# LPG - Light Projects Generator, a simple python package for lazy web
# developers ;)
#
# utilities.py :
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

# ASCII colors used :
#   yellow = \033[33m
#   red = \033[31m
#   green = \033[32m
#   cyan = \033[36m
#   underlined cyan = \033[4;36m
#   bright cyan = \033[1;96m

""" Contains pcolor(), print_yes() and print_no() """
def pcolor(message, color):
    """ Color print outputs in red, green, cyan, bright cyan, yellow and
    underlined cyan """
    if color == "yellow":
        return print("\033[33m{}\033[0m".format(message))
    if color == "red":
        return print("\033[31m{}\033[0m".format(message))
    if color == "bright_cyan":
        return print("\033[1;96m{}\033[0m".format(message))
    if color == "cyan":
        return print("\033[36m{}\033[0m".format(message))
    if color == "green":
        return print("\033[32m{}\033[0m".format(message))
    if color == "u_cyan":
        return print("\033[4;36m{}\033[0m".format(message))
    return print("\033[0m{}".format(message))

def print_yes():
    """ Print a green 'Yes' using pcolor """
    return pcolor("Yes", "green")

def print_no():
    """ Print a red 'No' using pcolor """
    return pcolor("No", "red")
