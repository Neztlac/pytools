import os
import requests

os.system("clear")

def get_ip():
    
    try:
        response = requests.get(url="https://api.ipify.org?format=json").json()
        return response.get('ip')
    except Exception:
        return "boudin"

ip = get_ip()

print(ip)

input()
