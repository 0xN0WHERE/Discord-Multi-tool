import os
import time
import requests
import sys
from config.settings import *

def webhook_edit():
        os.system("cls")
        Slow(discord_banner)
        time.sleep(1.5)
        os.system("cls")
        print(f"{bracketopen}!{bracketclosed} {Fore.BLUE}Webhook editor{Style.RESET_ALL}")
        print("")
        webhook_url = input(f"{bracketopen}>{bracketclosed} {Fore.BLUE}Webhook URL -> {Style.RESET_ALL}")
        webhook_name = input(f"{bracketopen}>{bracketclosed} {Fore.BLUE}New webhook name -> {Style.RESET_ALL}")

        try:
            response = requests.get(webhook_url)

            print("")

            if response.status_code == 200:
                try:
                    requests.patch(webhook_url, json={
                        "name": webhook_name
                    })

                    print(f"{bracketopen}~{bracketclosed} {Fore.BLUE}Renaming webhook... {Style.RESET_ALL}")
                    time.sleep(1.5)

                    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
                    time.sleep(0.05)
                    print(f"{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Renamed webhook to : {Style.RESET_ALL}{webhook_name}")
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