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
            spam_gc()
        elif command == "8" or command == "08":
            gen_invite()
        elif command == "9" or command == "09":
            lookup_server()
            
main()