#!/usr/bin/env python3
# Author: AuxGrep
# 2023
# 

"""
Techinique hii imekuwa famous sanaa na baadhi ya wadukuzi ili wasiweze kugundulika.
kupitia hii control server itaonesha ni namna gani invyoweza change IP kwa kila request
sent to destination server kupitia chamber za TOR (node1 , node 2 na exit node 3).
By default inachange ip kwa kila 10 sec ila kama unataka kupunguza edit time.sleep(10) to 
time.sleep(5) kwenye line namba 131, server hii inatumia proxychains kufanya kila kitu 
mfano ku ping kila request kwenye control server kucheck kama IP iko changed kabla request
hazijatoka nje na kwenda kwa target

OS SUPPORTED: LInux, Ubuntu, ParrotSec, ArchLinux

USAGE: 
       1. sudo chmod +x setup.sh && sudo bash setup.sh
       2. sudo python3 control_server.py 
       3. mfano unataka kurun nmap scan utatumia "sudo proxychains4 nmap -p 1-9999 -Pn" au
       unatak kufungua browser utatumia "proxychains firefox https://google.com" kila kitu
       kitakuwa under proxies na itakuwa inachane ip kwa kila 5-10 sec
"""
import time # hii ni kwa ajili ya sleeping time
import os # hii ni kwa ajili ya kucommunicate internal linux commands and kernel over flow
import sys # hii tutaitumia kwenye conditions statements
import requests # hii kwa ajili ya network requests (GET/POST)
import platform # hii ya kuchek platform os (mfumo endeshaji (windows/Linux))
import urllib.request # hii tutaituia kwa ajili ya testing ndogondogo za kuping kwenye server 
import subprocess # hii naitumia ili niweze start child na parrent process ikiwa na some basic commands
from fake_useragent import UserAgent # kwa ajili ya kufake mtumiaji wa control server - wee need fake natural traffics bro :)
from stem import Signal # stem tunaitumia kuhakikisha tunaforce tunnel ichange ip kadri tunavyotaka
from stem.control import Controller # anonymity IP controller

# colors
ITALIC = "\033[3m"
purple = '\x1b[38;5;165m'
blue = '\x1b[38;5;33m'
red = '\x1b[38;5;196m'
green = '\x1b[38;5;118m'
grey = '\x1b[38;5;0m'
pink = '\x1b[38;5;199m'
END = "\033[0m"
UNDERLINE = "\033[4m"
BOLD = "\033[1m"
BLINK = "\033[5m"



# I need root access !! let's check
if not os.geteuid() == 0:
    sys.exit("{0}{3}{2}\nOnly root can run this script\n{4}".format(BOLD, BLINK, ITALIC, red, END))


# CONTROL SERVER CONFIGURATIONS
ip_check_website = 'https://ident.me' # website to check public ip kama iko changed kwa kila 10sec
network_test_website = 'https://google.com' # change this na weka any internal access or external one


class control_server(): 
    # STEP 1: checking os 
    operating_system = platform.system()
    try:

        if operating_system != 'Linux':
            print('{0}{1}{2}Hey Bro!! control server support only Linux!! Exiting!!{3}'.format(BOLD, red, ITALIC, END))
            time.sleep(2)
            sys.exit()
        else:
            pass

        # STEP 2: Backup and Modifying Tor config file 
        check_tor_file = os.path.exists('/etc/tor/torrc')
        if check_tor_file == True:
            subprocess.run('sudo cp /etc/tor/torrc /opt', shell=True) # backing up to opt directory (cd /opt)
            if os.path.exists('/opt/torrc') == True:
                pass
            else:
                sys.exit('{0}{1}\nGot some Error2: torrc not found in the directory /opt{2}'.format(BOLD, red, END))
        else:
            print('{0}{1}{2}We need tor config file!! lets install it{3}'.format(BOLD, red, ITALIC, END))
            os.system('sudo apt-get install tor')
            os.system('clear')
            sys.exit('\nRun Again the script')

        # We need to add something kwenye config file la tor
        with open('/etc/tor/torrc', mode='a') as config_tor_network_file:
            config_tor_network_file.write('ControlPort 9051')
            config_tor_network_file.write('\nCookieAuthentication 1')

        # Also tunahitaji kumodify proxychains4 config file 
        proxychains4 = os.path.exists('/etc/proxychains.conf')
        if proxychains4 == True:
            os.system('sudo cp /etc/proxychains.conf /opt')
            time.sleep(2)
            with open('/etc/proxychains.conf', mode='a') as proxy_network_file:
                proxy_network_file.write('dynamic_chain') # dynamic chain kwasbb tunataka kila request iende na IP yake
                proxy_network_file.write('\nsocks5	127.0.0.1 9050') # Dont change port plz
        else:
            print('proxychains4 config file not in directory!! trying to fix!!')
            time.sleep(2)
            os.system('sudo apt-get install proxychains > /dev/null')
            sys.exit('\nRun Again the script')

        # STEP 3: checking Network connectivity
        def network_check(network_ping=f'{network_test_website}'):
            try:
                urllib.request.urlopen(network_ping)
                return True
            except:
                return False

        if network_check():
            os.system('clear')
            print(f'{BOLD}{green}{ITALIC}WELCOME TO PROXY-IP ROTATING CONTROL SERVER{END}'.center(100))
            print('')
            print(f'{BOLD}[*] Starting Tor....{END}')
            os.system('sudo service tor start > /dev/null')
            time.sleep(2)
            proxies = {
                    'http':'socks5://127.0.0.1:9050', #TOR ni best choice for both internal and external networks
                    'https':'socks5://127.0.0.1:9050'
                    }
            time.sleep(2)
            os.system('clear')
            print(f'{BOLD}{purple}**** CONTROL SERVER-IP ROTATING STARTED ****{END}'.center(100))
            print('')
            print("Changing IP Address in every 10 seconds....\n\n")
            while True:
                headers = { 'User-Agent': UserAgent().random }
                time.sleep(10) # badirisha hii to 5 kama unataka ip iwe inachange kwa kila 5 sec
                with Controller.from_port(port = 9051) as mandonga_mtu_kazi:
                    mandonga_mtu_kazi.authenticate()
                    mandonga_mtu_kazi.signal(Signal.NEWNYM)
                    print(f"Your IP is : {requests.get(f'{ip_check_website}', proxies=proxies, headers=headers).text}  ||  User Agent is : {headers['User-Agent']}")
        else:
            print('{0}{1}Error:Network issue detected!! Exiting!!!{2}'.format(BOLD, red, END))
            time.sleep(1)
            sys.exit()

    except KeyboardInterrupt:
        os.system('clear')
        # NORMAL exit
        if os.path.exists('/etc/tor/torrc') == True:
            print(f'{BOLD}{pink}{ITALIC}Restoring Tor + proxychains4 config files to normal{END}')
            os.system('sudo rm /etc/tor/torrc > /dev/null')
            time.sleep(2)
            os.system('sudo cp /opt/torrc /etc/tor')
            os.system('sudo rm /opt/torrc')
            time.sleep(1)
            os.system('sudo rm /etc/proxychains.conf')
            time.sleep(2)
            os.system('sudo cp /opt/proxychains.conf /etc')
            os.system('sudo rm /opt/proxychains.conf')
            os.system('sudo service tor stop')
            sys.exit(f'{BOLD}user cancelled!! bYEEEE!!{END}')
        # Fast Exiting
        else:
            os.system('clear')
            sys.exit('byee')

