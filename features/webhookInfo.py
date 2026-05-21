import os
import time
import requests
import sys
from config.settings import *

def webhook_info():
        os.system("cls")
        Slow(discord_banner)
        time.sleep(1.5)
        os.system("cls")
        print(f"{bracketopen}!{bracketclosed} {Fore.BLUE}Webhook lookup{Style.RESET_ALL}")
        print("")
        webhook_url = input(f"{bracketopen}>{bracketclosed} {Fore.BLUE}Webhook URL -> {Style.RESET_ALL}")

        try:
            response = requests.get(webhook_url)

            print("")

            if response.status_code == 200:
                try:
                    data = response.json()
                    print(f"{bracketopen}~{bracketclosed} {Fore.BLUE}Getting webhook information... {Style.RESET_ALL}")
                    time.sleep(1.5)

                    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
                    time.sleep(0.05)
                    print(f"{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Name       : {Style.RESET_ALL}{data['name']}")
                    time.sleep(0.05)
                    print(f"{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} ID         : {Style.RESET_ALL}{data['id']}")
                    time.sleep(0.05)
                    print(f"{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Token      : {Style.RESET_ALL}{data['token']}")
                    time.sleep(0.05)
                    print(f"{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Avatar     : {Style.RESET_ALL}{data['avatar']}")
                    time.sleep(0.05)
                    print(f"{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Channel ID : {Style.RESET_ALL}{data['channel_id']}")
                    time.sleep(0.05)
                    print(f"{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Guild ID   : {Style.RESET_ALL}{data.get('guild_id')}")
                    time.sleep(0.05)
                    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")

                except Exception:
                    print(f"{bracketopen2}{Fore.BLUE}!{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Webhook unavailable{Style.RESET_ALL}")
                    time.sleep(2)
                    return
            else:
                time.sleep(0.05)
                print(f"{bracketopen2}{Fore.BLUE}!{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Webhook unavailable{Style.RESET_ALL}")
                time.sleep(2)
                return


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
            print("")
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.BLUE} Invalid URL{Style.RESET_ALL}")
            time.sleep(2)