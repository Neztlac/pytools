import os

def pause():
    try:
        input("")
    except Exception:
        return "caca"

def clear():
    try:
        os.system("clear")
    except Exception:
        return "caca"

menu = True

while menu:

    clear()
    

    print("                       _        _ _ ")
    print(" _ __  _   _ _ __  ___| |_ __ _| | | ___ _ __")
    print("| '_ \| | | | '_ \/ __| __/ _` | | |/ _ \ '__|")
    print("| |_) | |_| | | | \__ \ || (_| | | |  __/ | ")
    print("| .__/ \__, |_| |_|___/\__\__,_|_|_|\___|_|")
    print("|_|    |___/")

    print("")
    print("Bienvenue dans PYNSTALLER !")

    choix = input("Veuillez selectionner une option\n\n[1] : SpeedTest\n[2] : Neofetch\n[3] : NeoVim\n[4] : Fish\n[5] : Discord\n[6] : Telegram\n[7] : Gparted\n[8] : Htop\n[9] : Snap\n\n[0] : TOUT !\n\n[Q] : Quitter\n\n> ") 

    if choix == '1':
        clear()
        os.system("sudo apt -y install speedtest-cli")
        pause()
    elif choix == '2':
        clear()
        os.system("sudo apt -y install neofetch")
        pause()
    elif choix == '3':
        clear()
        os.system("sudo apt -y install neovim")
        pause()
    elif choix == '4':
        clear()
        os.system("sudo apt -y install fish")
        pause()
    elif choix == '5':
        clear()
        os.system("sudo apt -y install discord")
        pause()
    elif choix == '6':
        clear()
        os.system("sudo apt -y install telegram-desktop")
        pause()
    elif choix == '7':
        clear()
        os.system("sudo apt -y install gparted")
        pause()
    elif choix == '8':
        clear()
        os.system("sudo apt -y install htop")
        pause()
    elif choix == '9':
        clear()
        os.system("sudo apt -y install snapd")
        pause()
    elif choix == '0':
        clear()
        os.system("sudo apt -y install speedtest-cli neofetch neovim fish discord telegram-desktop gparted htop snapd")
        pause()
    elif choix == 'q':
        exec(open("./main.py").read())
