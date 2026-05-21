import os
import time
import requests
from datetime import datetime
import sys
from config.settings import *

def token_info():
    os.system("cls")
    Slow(discord_banner)
    time.sleep(1.5)
    os.system("cls")
    print(f"{bracketopen}!{bracketclosed} {Fore.BLUE}Token checker{Style.RESET_ALL}")
    print("")
    token = input(f"{bracketopen}>{bracketclosed} {Fore.BLUE}Token -> {Style.RESET_ALL}")
    print("")

    languages = {
        'da'    : 'Danish, Denmark',
        'de'    : 'German, Germany',
        'en-GB' : 'English, United Kingdom',
        'en-US' : 'English, United States',
        'es-ES' : 'Spanish, Spain',
        'fr'    : 'French, France',
        'hr'    : 'Croatian, Croatia',
        'lt'    : 'Lithuanian, Lithuania',
        'hu'    : 'Hungarian, Hungary',
        'nl'    : 'Dutch, Netherlands',
        'no'    : 'Norwegian, Norway',
        'pl'    : 'Polish, Poland',
        'pt-BR' : 'Portuguese, Brazilian, Brazil',
        'ro'    : 'Romanian, Romania',
        'fi'    : 'Finnish, Finland',
        'sv-SE' : 'Swedish, Sweden',
        'vi'    : 'Vietnamese, Vietnam',
        'tr'    : 'Turkish, Turkey',
        'cs'    : 'Czech, Czechia, Czech Republic',
        'el'    : 'Greek, Greece',
        'bg'    : 'Bulgarian, Bulgaria',
        'ru'    : 'Russian, Russia',
        'uk'    : 'Ukranian, Ukraine',
        'th'    : 'Thai, Thailand',
        'zh-CN' : 'Chinese, China',
        'ja'    : 'Japanese',
        'zh-TW' : 'Chinese, Taiwan',
        'ko'    : 'Korean, Korea'
    }

    try:
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }

        res = requests.get('https://discordapp.com/api/v9/users/@me', headers=headers)

        if res.status_code == 200:
            res_json = res.json()

            user_name = f'{res_json["username"]}'
            user_id = res_json['id']
            phone_number = res_json['phone']
            email = res_json['email']
            locale = res_json['locale']
            nsfw_allowed = res_json['nsfw_allowed']

            if nsfw_allowed is True:
                nsfw_allowed = "Allowed"
            else:
                nsfw_allowed = "Not allowed"
            
            language = languages.get(locale)

            creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')

            has_nitro = False
            res = requests.get('https://discordapp.com/api/v9/users/@me/billing/subscriptions', headers=headers)
            if res.status_code == 200:
                nitro_data = res.json()
                has_nitro = bool(len(nitro_data) > 0)
                if has_nitro:
                    d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                    d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                    days_left = abs((d2 - d1).days)

                billing_info = []
                for x in requests.get('https://discordapp.com/api/v9/users/@me/billing/payment-sources', headers=headers).json():
                    y = x.get('billing_address') or {}
                    data = None

                    name = y.get('name', '')
                    ...
                    
                    if x['type'] == 1:
                        data = {
                            ...
                        }

                    elif x['type'] == 2:
                        data = {
                            ...
                        }

                    if data is not None:
                        billing_info.append(data)
                    name = y.get('name', '')
                    city = y.get('city', '')
                    state = y.get('state', '')
                    country = y.get('country', '')
                
                print(f"{bracketopen}~{bracketclosed} {Fore.BLUE}Getting token information... {Style.RESET_ALL}")
                time.sleep(1.5)
                print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
                time.sleep(0.05)
                print(f'{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Username        :{Style.RESET_ALL}   {user_name}')
                time.sleep(0.05)
                print(f'{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} User ID         :{Style.RESET_ALL}   {user_id}')
                time.sleep(0.05) 
                print(f'{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Token           :{Style.RESET_ALL}   {token}')
                time.sleep(0.05)  
                print(f'{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Creation date   :{Style.RESET_ALL}   {creation_date}')
                time.sleep(0.05)
                print(f'{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Country         :{Style.RESET_ALL}   {language}')
                time.sleep(0.05)

                print("")
                time.sleep(0.05)
                print(f'{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Phone number    :{Style.RESET_ALL}   {phone_number if phone_number else "None"}')
                time.sleep(0.05)
                print(f'{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Email           :{Style.RESET_ALL}   {email if email else "None"}')
                time.sleep(0.05)
                print("")

                if not has_nitro:
                    print(f'{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Nitro status    :{Style.RESET_ALL}   No nitro')
                    print("")
                if has_nitro:
                    print(f'{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Expires in      :{Style.RESET_ALL}   {days_left} day(s)')
                    print("")
    
                print(f'{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} NSFW            :{Style.RESET_ALL}   {nsfw_allowed}')

                if billing_info:
                    print("")
                    print(f'{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Name              :{Style.RESET_ALL}   {name}')
                    time.sleep(0.05)
                    print(f'{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} Country           :{Style.RESET_ALL}   {country}')
                    time.sleep(0.05)
                    print(f'{bracketopen2}{Fore.BLUE}+{Style.RESET_ALL}{bracketclosed2}{Fore.BLUE} City              :{Style.RESET_ALL}   {city}')
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
                print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.BLUE} Invalid token{Style.RESET_ALL}")
                time.sleep(2)
                return                             

        else:
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.BLUE} Invalid token{Style.RESET_ALL}")
            time.sleep(2)
            return

    except Exception as e:
        print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.BLUE} Invalid token{Style.RESET_ALL}")
        time.sleep(2)
        return
