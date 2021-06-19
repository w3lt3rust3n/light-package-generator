#! /bin/bash -e

echo "HELLO FROM REACT SCRIPT"
echo "The project will be located at $1 and the name is $2"
cd $1 &&
npx create-react-app $2
echo "Should be good"
