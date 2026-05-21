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

line1 = f"{Fore.BLUE}|{Style.RESET_ALL}"
line2 = f"{Fore.WHITE}|{Style.RESET_ALL}"

Next = f"{bracketopen}+{bracketclosed} Next"
Back = f"{bracketopen}+{bracketclosed} Back"

response = requests.get("https://api.ipify.org")
public_ip = response.text

system_version = platform.platform()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
 s.connect(("8.8.8.8", 80))
 private_ip = s.getsockname()[0]
finally:
 s.close()

mac_get = uuid.getnode()
mac = ':'.join(f"{(mac_get >> ele) & 0xff:02x}" for ele in range(40, -1, -8))

pc_name = platform.node()
username = os.getlogin()

is_windows = os.name == "nt"
system_text = "Windows" if is_windows else "Linux"

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