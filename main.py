import os
from functions.webhookDel import *
from functions.webhookSpam import *
from functions.webhookInfo import *
from functions.webhookEdit import *
from functions.tokenInfo import *
from functions.tokenNuke import *
from functions.inviteGen import *
from functions.groupSpammer import *
from functions.serverInfo import *

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

def main():
    while True:
        os.system("cls")
        Slow(banner)
        print("")
        Slow(menu1)
        
        command = input(f"""{Fore.BLUE} ┌──({Fore.WHITE}{username}{Fore.BLUE})─[{Fore.WHITE}~/{system_text}/{pc_name}{Fore.BLUE}]
 └─{Fore.WHITE}$ {Style.RESET_ALL}""")
                
        if command == "1" or command == "01":
            delete_webhook()
        elif command == "2" or command == "02":
            WebhookSpam()
        elif command == "3" or command == "03":
            webhook_edit()
        elif command == "4" or command == "04":
            webhook_info()
        elif command == "5" or command == "05":
            token_info()
        elif command == "6" or command == "06":
            nuke_token()
        elif command == "7" or command == "07":
            pass
        elif command == "8" or command == "08":
            spam_gc()
        elif command == "9" or command == "09":
            gen_invite()
        elif command == "10":
            lookup_server()
            
main()
