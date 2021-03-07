#/bin/bash

clear

sudo apt -y install fish

mkdir ~/Documents/code
mkdir ~/Documents/code/python
mkdir ~/Documents/code/python/pytools

cp *.* ~/Documents/code/python/tools

cd ~/Documents/code/python/pytools

./fishAliasList.sh

chsh -s /usr/bin/fish
