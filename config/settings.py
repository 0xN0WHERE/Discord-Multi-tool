from colorama import Fore, Back, Style, init
import requests
import os
import socket
import platform
import uuid
import time

bracketopen = f"{Fore.BLUE}[{Style.RESET_ALL}"
bracketclosed = f"{Fore.BLUE}]{Style.RESET_ALL}"

bracketopen2 = f"{Fore.WHITE}[{Style.RESET_ALL}"
bracketclosed2 = f"{Fore.WHITE}]{Style.RESET_ALL}"

response = requests.get("https://api.ipify.org")
public_ip = response.text

system_version = platform.platform()

pc_name = platform.node()
username = os.getlogin()

is_windows = os.name == "nt"
system_text = "Windows" if is_windows else "Linux"

banner = f"""{Fore.BLUE}
                    ________  .__                              .___   __                .__   
                    \______ \ |__| ______ ____  ___________  __| _/ _/  |_  ____   ____ |  |  
                     |    |  \|  |/  ___// ___\/  _ \_  __ \/ __ |  \   __\/  _ \ /  _ \|  |  
                     |    `   \  |\___  \  \__(  <_> )  | \/ /_/ |   |  | (  <_> |  <_> )  |__
                    /_______  /__/____  >\___  >____/|__|  \____ |   |__|  \____/ \____/|____/
                            \/        \/     \/                 \/                     
                                                ~ https://github.com/0xN0WHERE                                                                                  
          {Style.RESET_ALL}                            
"""

title1 = "Webhooks"
title2 = "User"
title3 = "Server"

#Webhooks
webhook_deleter = f"{bracketopen}01{bracketclosed} Webhook deleter"
webhook_spam = f"{bracketopen}02{bracketclosed} Webhook spammer"
webhook_editor = f"{bracketopen}03{bracketclosed} Webhook editor"
webhook_informations = f"{bracketopen}04{bracketclosed} Webhook info"

#User
token_infos = f"{bracketopen}05{bracketclosed} User token checker"
token_spammer = f"{bracketopen}06{bracketclosed} User token nuker"
gc_spammer = f"{bracketopen}07{bracketclosed} Groupchat spammer"

#Server
invite_gen = f"{bracketopen}08{bracketclosed} Bot invite gen"
server_info = f"{bracketopen}09{bracketclosed} Server info"

menu1 = f"""{Fore.BLUE}
              ┌──────────────────┐                        ┌──────────┐                       ┌──────────┐ 
   ┬──────────┤     {Style.RESET_ALL}{title1} {Fore.BLUE}    ├─────────┬──────────────┤   {Style.RESET_ALL}{title2} {Fore.BLUE}  ├────────────┬──────────┤  {Style.RESET_ALL}{title3} {Fore.BLUE} ├──────────┬
   │          └──────────────────┘         │              └──────────┘            │          └──────────┘          │
   ├─ {Style.RESET_ALL}{webhook_deleter} {Fore.BLUE}                ├─ {Style.RESET_ALL}{token_infos} {Fore.BLUE}            ├─ {Style.RESET_ALL}{invite_gen} {Fore.BLUE}          │
   ├─ {Style.RESET_ALL}{webhook_spam} {Fore.BLUE}                ├─ {Style.RESET_ALL}{token_spammer} {Fore.BLUE}              ├─ {Style.RESET_ALL}{server_info} {Fore.BLUE}             │
   ├─ {Style.RESET_ALL}{webhook_editor} {Fore.BLUE}                 ├─ {Style.RESET_ALL}{gc_spammer} {Fore.BLUE}             ├─                               │
   ├─ {Style.RESET_ALL}{webhook_informations} {Fore.BLUE}                   └─                                     └─                               │
   ├─                                                                                               
   └─ 
            {Style.RESET_ALL}                                                         
"""

discord_banner = (f"""{Fore.BLUE}
                                              @@@@                @%@@                                      
                                       @@@@@@@@@@@@               @@@@@@@@@@%                               
                                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                          
                                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                         
                                %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                        
                               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                       
                              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                      
                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                     
                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                    
                           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                   
                          %@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@%                  
                          %@@@@@@@@@@@@@@@@        %@@@@@@@@@@@%@        @@@@@@@@@@@@@@@@@                  
                          %@@@@@@@@@@@@@@@          @@@@@@@@@@@@          @@@@@@@@@@@@@@@%                  
                         %@@@@@@@@@@@@@@@@          @@@@@@@@@@@%          %@@@@@@@@@@@@@@@@                 
                         @@@@@@@@@@@@@@@@@%         @@@@@@@@@@@%         %@@@@@@@@@@@@@@@@@                 
                         @@@@@@@@@@@@@@@@@@@      %@@@@@@@@@@@@@@@      @@@@@@@@@@@@@@@@@@%                 
                         %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                 
                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                 
                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                 
                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                 
                           @%@@@@@@@@@@@@@%@@   @@@@%@@@@@@@@@%%%@%@@  @@@@@@@@@@@@@@@@@@                   
                              @@%@@@@@@@@@@@@@                        @%@@@@@@@@@@@%@@                      
                                   @%@@@@@@@                            @@@@@@%%@                           
                                         @@                              @@        
{Style.RESET_ALL}                                     
""")

def Slow(banner):
    delai = 0.03
    lignes = banner.split('\n')
    for ligne in lignes:
        print(ligne)
        time.sleep(delai)