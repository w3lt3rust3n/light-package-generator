#! /bin/bash -e

#------------------------------------------------------------------------------
# LPG - Light Projects Generator, a simple python package for lazy web
# developers ;)
#
# lpg-flutter-init.sh :
# Launched by option -g flutter.
#
# Made with love by Maxence Buisson for the fun of it.
# Contact : weltrusten@philentropy.org
#
# Enjoy !
#------------------------------------------------------------------------------

cd "$1" &&
flutter channel stable &&
flutter upgrade &&
flutter create "$2"
