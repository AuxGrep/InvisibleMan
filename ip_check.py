import time
import os as startscan

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


def IP():
    try:
        print(f'{BOLD}{purple}{ITALIC}Checking Your Public/private IP for every 5 sec{END}'.center(100))
        print('')
        while True:
            req = startscan.system('sudo proxychains curl http://checkip.amazonaws.com')
            time.sleep(5)
    except OSError:
        print('{BOLD}{red}Network issue: Control server is down!!{END}')
IP();
