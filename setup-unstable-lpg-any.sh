#! /bin/bash -e

echo "LIGHT PACKAGE GENERATOR INSTALLER"
home=$HOME
echo "$home"
echo "Copy lpg..."
cp -Rv lpg "$home" &&
cd "$home" &&
echo "Renaming lpg..." &&
mv -v lpg .lpg &&
echo "Preparing scripts..."
cd .lpg/scripts &&
chmod +x lpg-*.sh
echo "Done, run src/main.py -h, --help"