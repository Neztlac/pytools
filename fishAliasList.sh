#!/bin/bash

fish << 'END_FISH'

#SOFTWARE
alias v="nvim"
alias py="python3"
alias ssavr="firefox ssavr.com"

#LINUX COMMANDS
alias rmr="rm -r"
alias install="sudo apt -y install"
alias uu="sudo apt -y update && sudo apt -y upgrade"
alias shutdown="sudo shutdown now"
alias remove="sudo apt -y remove"

#FUNCSAVE

funcsave v
funcsave py
funcsave ssavr
funcsave rmr
funcsave install
funcsave uu
funcsave shutdown
funcsave remove

END_FISH
