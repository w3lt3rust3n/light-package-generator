#! /bin/bash -e

echo "HELLO FROM flutter script"
echo "The project will be located at $1 and the name is $2"
cd $1 &&
flutter channel stable &&
flutter upgrade &&
flutter create $2
