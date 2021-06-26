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

def pcolor(message, color):
    """gngngn"""
    if color == "yellow":
        return print("\033[33m{}\033[0m".format(message))
    if color == "bright_cyan":
        return print("\033[1;96m{}\033[0m".format(message))
    if color == "cyan":
        return print("\033[36m{}\033[0m".format(message))
    if color == "green":
        return print("\033[32m{}\033[0m".format(message))
    if color == "u_cyan":
        return print("\033[4;36m{}\033[0m".format(message))
    return None

def print_yes():
    """gngngn"""
    return pcolor("Yes")

def print_no():
    """gngngn"""
    return pcolor("No")