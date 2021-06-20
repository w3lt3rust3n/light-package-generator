#! /bin/bash -e

cd $1 &&
flutter channel stable &&
flutter upgrade &&
flutter create $2
