import random
import requests

from colorama import Fore



ip_input = input("Enter IP address: ")


def lookup():
    
    headers = {
        'authority': 'ipinfo.io',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        'referer': 'https://ipinfo.io/',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        }
    r = requests.get(f'https://ipinfo.io/widget/demo/{ip_input}', headers=headers)
    ip = r.json()['data']['ip']
    city = r.json()['data']['city']
    region = r.json()['data']['region']
    country = r.json()['data']['country']
    timezone = r.json()['data']['timezone']
    address = r.json()['data']['abuse']['address']
    country = r.json()['data']['abuse']['country']
    print(f'{Fore.YELLOW}IP: {Fore.RESET}{ip}')
    print(f'{Fore.YELLOW}City: {Fore.RESET}{city}')
    print(f'{Fore.YELLOW}Region: {Fore.RESET}{region}')
    print(f'{Fore.YELLOW}Country: {Fore.RESET}{country}')
    print(f'{Fore.YELLOW}Timezone: {Fore.RESET}{timezone}')
    print(f'{Fore.YELLOW}Address: {Fore.RESET}{address}')


lookup()