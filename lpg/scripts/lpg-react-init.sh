#! /bin/bash -e

#------------------------------------------------------------------------------
# LPG - Light Projects Generator, a simple python package for lazy web
# developers ;)
#
# lpg-react-init.sh :
# Launched by option -g react.
#
# Made with love by Maxence Buisson for the fun of it.
# Contact : weltrusten@philentropy.org
#
# Enjoy !
#------------------------------------------------------------------------------

cd "$1" &&
npx create-react-app "$2"