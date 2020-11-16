import os

def pause():
    try:
        input('')
    except SyntaxError:
        pass

os.system("clear")
os.system("htop")

pause()