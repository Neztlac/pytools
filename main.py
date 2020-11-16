import os
import requests

Main = True

def pause():
    try:
        input('')
    except SyntaxError:
        pass

def clearscreen():
    try:
        os.system("clear")
    except SyntaxError:
        pass

while Main:

    clearscreen()

    print(" _____ ___   ___  _     ____  ")
    print("|_   _/ _ \ / _ \| |   / ___| ")
    print("  | || | | | | | | |   \___ \ ")
    print("  | || |_| | |_| | |___ ___) |")
    print("  |_| \___/ \___/|_____|____/ ")

    print("")

    print("Random motivational phrase of the day : ")

    def get_affirmation():
    
        try:
            response = requests.get(url="https://www.affirmations.dev").json()
            return response.get('affirmation')
        except Exception:
            return "caca"

    affirmation = get_affirmation()

    print(affirmation)

    print('')
    print('Pick a tool !\n')

    choix = input('[1] : Ping\n[2] : My Public IP\n[3] : My Local IP\n[4] : Neofetch\n[5] : htop\n\n[6] : PYNSTALLER\n\n[Q] : Quit\n\n: ')

    if choix == '1':
        exec(open("./ping.py").read())
    elif choix == '2':
        exec(open("./public_ip.py").read())
    elif choix == '3':
       exec(open("./local_ip.py").read())
    elif choix == '4': #quite direct ptdr
       exec(open("./neofetch.py").read())
    elif choix == '5': 
       exec(open("./htop.py").read())
    elif choix == '6':
       exec(open("./pynstaller.py").read())
    elif choix == '7':
       exec(open("./pyFunc.py").read())
    elif choix == 'q':
        #menu = 0
        clearscreen()
        exit()
