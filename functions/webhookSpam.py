import os
import time
import requests
import sys
from config.settings import *

def WebhookSpam():
            os.system("cls")
            Slow(discord_banner)
            time.sleep(1.5)
            os.system("cls")
            print(f"{bracketopen}!{bracketclosed} {Fore.BLUE}Webhook spammer{Style.RESET_ALL}")
            print("")   
            webhook = input(f"{bracketopen}>{bracketclosed} {Fore.BLUE}Webhook URL -> {Style.RESET_ALL}")

            try:
                r = requests.get(webhook)
                if r.status_code == 200:      
                    spamtext = input(f"{bracketopen}>{bracketclosed} {Fore.BLUE}Spamtext -> {Style.RESET_ALL}")

                    try:
                        words = int(input(f"{bracketopen}>{bracketclosed} {Fore.BLUE}Number of messages-> {Style.RESET_ALL}"))

                        message = {
                                "content": spamtext
                            }

                        if words > 100:
                                print("")
                                print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.BLUE} Number of messages too high{Style.RESET_ALL}")
                                time.sleep(2)
                        elif words < 1:
                                print("")
                                print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.BLUE} Number of messages too low{Style.RESET_ALL}")
                                time.sleep(2)
                        else:
                            print("")
                            print(f"{bracketopen}~{bracketclosed} {Fore.BLUE}Spamming webhook... {Style.RESET_ALL}")
                            time.sleep(0.05)
                            try:
                                for i in range(words):
                                        response = requests.post(webhook, json=message)
                                print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
                                print(f"{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Webhook got spammed{Style.RESET_ALL}")
                            except Exception:
                                print(f"{bracketopen2}{Fore.BLUE}!{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Error spamming webhook{Style.RESET_ALL}")
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
                        print("")
                        print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.BLUE} Invalid number{Style.RESET_ALL}")
                        time.sleep(2)

                else:
                    print("")
                    print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.BLUE} Invalid URL{Style.RESET_ALL}")
                    time.sleep(2)

            except Exception:
                print("")
                print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.BLUE} Invalid URL{Style.RESET_ALL}")
                time.sleep(2)
            

 