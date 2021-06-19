#! /bin/bash -e

echo "HELLO FROM SYMFONY SCRIPT"
cd $1 &&
composer create-project symfony/website-skeleton $2
echo "Should be done"
