#! /bin/bash -e

#------------------------------------------------------------------------------
# LPG - Light Projects Generator, a simple python package for lazy web
# developers ;)
#
# lpg-symfony-init.sh :
# Launched by option -g symfony.
#
# Made with love by Maxence Buisson for the fun of it.
# Contact : weltrusten@philentropy.org
#
# Enjoy !
#------------------------------------------------------------------------------

cd "$1" &&
composer create-project symfony/website-skeleton "$2"

