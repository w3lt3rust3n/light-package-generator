#! /bin/bash -e
#
cat $1 | head -n 1 > $2
#echo $2