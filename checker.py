from os import system
import requests , uuid , time 
import os
import time
from colorama import Fore, Back, Style
import sys
import json
import random


if sys.version_info[0] < 3:
	pyversion = python_version()
	print("Alert! Your python version is %s. Use python version 3> to run this code" %(pyversion))
	exit(1)

req = requests.session()
uid = uuid.uuid4()
system("title " + "t.me/undecryptable")
os.system('cls||clear')
print(Back.BLACK + Fore.MAGENTA + '              zeeeeee-\n            z$$$$$$"\n           d$$$$$$"\n          d$$$$$P\n         d$$$$$P\n        $$$$$$"\n      .$$$$$$"\n     .$$$$$$"\n    4$$$$$$$$$$$$$"\n   z$$$$$$$$$$$$$"\n   """""""3$$$$$"\n         z$$$$P\n        d$$$$"\n      .$$$$$"\n     z$$$$$"\n    z$$$$P\n   d$$$$$$$$$$"\n  *******$$$"\n       .$$$"\n      .$$"\n     4$P"\n    z$"\n   zP\n  z"')
print('')
print('')
print(Fore.CYAN + '          Critical Ops Name Checker by yin/who?')
print('')
print('')

r = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=200&country=all&ssl=all&anonymity=all")
scrape = open('proxies.txt', 'wb')
scrape.write(r.content)
scrape = open("proxies.txt", "r")
proxy = random.choice(open('proxies.txt').readlines())
scrape.close
proxies = {
        'http': 'http://' + proxy}
while True:
    file = open('user.txt', 'r')
    for user in file:
        
        data = {"usernames":[user.strip()]}
        headers = {
            'accept': '*/*',
            'content-type': 'application/json',
            'x-apiversion': '1.28.0.f1605',
            'authorization': 'Bearer NzI3MDY5MDczOjA3YTRiYzk5YmJmNThjYWM5NDM4NmVjMmZkY2Y0NjQwOjY5NzQ5MDk0NTpjMTc1ODI5N2M3OGNkNGU4Zjk2YjQ1ODljYWUzNGIyNzpBdG1pbnROb014UnF1UkR3Mk1sRVdOcXQ3UTdkVXRYNGIxQUVIK2taL091elEwc0UxdnBmdk1sS1duMVQ2MFYweDRZSitjNmpTaW1LRVp4ZEFsZ3lNUT09',
            'content-length': '21',
            'x-unity-version': '2020.3.19f1',
            'accept-language': 'en-ca',
            'user-agent': 'CriticalOps/1765 CFNetwork/1128.0.1 Darwin/19.6.0',
            'accept-encoding': 'gzip, deflate, br',
            'Host': '1-28-0.prod.copsapi.criticalforce.fi'}
        url = "https://1-28-0.prod.copsapi.criticalforce.fi/api/user/find/usernames/"
        res = requests.post(url,json=data,headers=headers,proxies=proxies)
        #print(res.text)
        #json_object = json.dumps(res.json(), indent = 4)
        #f = open(user.strip() + ".json", "w")
        #f.write(json_object)
        #f.close() this was for mass scraping
        if res.text == "Error 53":
            print(Fore.WHITE + "[" + Fore.MAGENTA + "+" + Fore.WHITE + "]" + Fore.MAGENTA + user.strip() + " Available")
            f = open("available" + ".txt", "a")
            f.write(user.strip() + "\n")
            f.close()
        else:
            print(Fore.WHITE + "[" + Fore.RED + "-" + Fore.WHITE + "]" + Fore.RED + user.strip() + " Not Available")
            
file.close
#note from Timer1337: "play stupid games win stupid prizes :)
#by yin/who?/timer/kevin
