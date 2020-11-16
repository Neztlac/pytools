import os

os.system("clear")

def local_ip():
    
    try:
        os.system('ip address | grep inet')
    except Exception:
        print("ptdr t ki")

ip = local_ip()

print(ip)

input("\n")
