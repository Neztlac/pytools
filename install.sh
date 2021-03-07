#/bin/bash

clear

sudo apt -y install fish

mkdir ~/Documents/code
mkdir ~/Documents/code/python
mkdir ~/Documents/code/python/tools

cp *.* ~/Documents/code/python/tools

cd ~/Documents/code/python/tools

./fishAliasList.sh

chsh -s /usr/bin/fish
