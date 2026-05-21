import os
import time
import requests
import sys
from config.settings import *

def lookup_server():
        os.system("cls")
        Slow(discord_banner)
        time.sleep(1.5)
        os.system("cls")
        print(f"{bracketopen}!{bracketclosed} {Fore.BLUE}Server lookup{Style.RESET_ALL}")
        print("")
        invite_link = input(f"{bracketopen}>{bracketclosed} {Fore.BLUE}Server invite -> {Style.RESET_ALL}")

        invite_code = invite_link.replace("https://discord.gg/", "").replace("http://discord.gg/", "").replace("discord.gg/", "").strip()

        try:
            res = requests.get(f"https://discord.com/api/v9/invites/{invite_code}")

            if res.status_code == 200:
                data = res.json()

                invite = f"https://discord.gg/{data['code']}"

                print("")
                print(f"{bracketopen}~{bracketclosed} {Fore.BLUE}Looking for information... {Style.RESET_ALL}")
                time.sleep(1.5)
                print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
                time.sleep(0.05)
                print(f"{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Name            :{Style.RESET_ALL} {data['guild']['name']}")
                time.sleep(0.05)
                print(f"{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Guild ID        :{Style.RESET_ALL} {data['guild']['id']}")
                time.sleep(0.05)
                print(f"{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Description     :{Style.RESET_ALL} {data['guild']['description']}")
                time.sleep(0.05)
                print(f"{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Banner          :{Style.RESET_ALL} {data['guild']['banner']}")
                time.sleep(0.05)
                print(f"{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Verify level    :{Style.RESET_ALL} {data['guild']['verification_level']}")
                time.sleep(0.05)

                print("")

                print(f"{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Invite link     :{Style.RESET_ALL} {invite}")
                time.sleep(0.05)
                print(f"{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Channel         :{Style.RESET_ALL} {data['channel']['name']} - ({data['channel']['id']})")
                time.sleep(0.05)
                print(f"{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Expiration date :{Style.RESET_ALL} {data['expires_at'].split('T')[0]}")
                time.sleep(0.05)

                print("")

                print(f"{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Inviter         :{Style.RESET_ALL} {data['inviter']['username']}")
                time.sleep(0.05)
                print(f"{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Inviter ID      :{Style.RESET_ALL} {data['inviter']['id']}")

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
            else:
                time.sleep(0.05)
                print(f"{bracketopen2}{Fore.BLUE}!{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Server unavailable{Style.RESET_ALL}")
                time.sleep(2)
                return

        except Exception:
            print("")
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.BLUE} Invalid invite link{Style.RESET_ALL}")
            time.sleep(2)
        