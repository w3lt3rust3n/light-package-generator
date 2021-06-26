#! /usr/bin/env python3
# coding: utf-8

#---------------------------------------------------------------------
# # LPG - Light Project Manager, a simple python program for lazy web
# developers ;)
#
# preparator.py : All that LPG needs to prepare system by installing
# dependencies or the framework/librarie using option -p.
#
# CAUTION : expect unexpected behaviors on Windows machines.
# May work as expected under GNU/Linux systems.
#
# Made with love by Maxence Buisson for the fun of it.
# Contact : weltrusten@philentropy.org
#
# Enjoy !
#---------------------------------------------------------------------
""" gngngn """
class Preparator:
    """ggngng"""
    LPG_DIR = ".lpg/"
    CONFIG_DIR = ".lpg/config"

    def __init__(self, lang):
        self.lang = lang

    def __load_conf_file(self):
        pass

    def init_preparator(self, lang):
        """ gngngngn """
        print("Hello from init_preparator, let's play with {}".format(lang))
