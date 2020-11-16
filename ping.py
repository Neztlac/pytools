import os

os.system("clear")

var_ping = input('Entrez une adresse : \n\n> ')

def ping(var_ping):

    os.system(f'ping -c 4 {var_ping}\n')

ping(var_ping)

input("")
