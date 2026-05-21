import logging
logging.disable(logging.CRITICAL)

import discord
import os
import time
import sys
from config.settings import *

client = discord.Client(intents=discord.Intents.default())

invites = []

def gen_invite():
        os.system("cls")
        Slow(discord_banner)
        time.sleep(1.5)
        os.system("cls")
        print(f"{bracketopen}!{bracketclosed} {Fore.BLUE}Invite generator{Style.RESET_ALL}")
        print("")
        token = input(f"{bracketopen}>{bracketclosed} {Fore.BLUE}Bot token -> {Style.RESET_ALL}")

        try:
            @client.event
            async def on_ready():
                for guild in client.guilds:
                    for channel in guild.text_channels:
                        perms = channel.permissions_for(guild.me)

                        if perms.create_instant_invite:
                            invite = await channel.create_invite()
                            invites.append(f"{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} {invite}  :  {Style.RESET_ALL}{guild.name}")
                            break

                await client.close()

            client.run(token)

            print("")
            print(f"{bracketopen}~{bracketclosed} {Fore.BLUE}Generating invite... {Style.RESET_ALL}")
            time.sleep(1.5)
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            time.sleep(0.05)
            for invite in invites:
                print(invite)
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
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.BLUE} Invalid token{Style.RESET_ALL}")
            time.sleep(2)