#-- coding: utf8 --
#!/usr/bin/python

import sys, os, logging
import platform, time
import subprocess
import socket
import argparse
from datetime import datetime
import importlib
try:

    import colorama
    colorama.init()
    from termcolor import *
except ImportError:
    import pip
    print('Downloading package dependencies')
    pip.main(['install', 'termcolor'])
    pip.main(['install', 'colorama'])
finally:
    import colorama
    colorama.init()
    from termcolor import *
    import site
    reload(site)
    globals()['termcolor'] = importlib.import_module('termcolor')
    globals()['colorama'] = importlib.import_module('colorama')


globals()['termcolor']
globals()['colorama']
logo = '''
                                    _       ___         _   
                          _ __  ___| |_ ___| _ \___ _ _| |_ 
                         | '_ \/ _ \  _/ _ \  _/ _ \ '_|  _|
                         | .__/\___/\__\___/_| \___/_|  \__|
                         |_|                                                                                                      
                                Author: Ph.03n1x
                                Github: https://github.com/whoami213/
                                Version: 1.3                           
'''

print(colored(logo, 'cyan', attrs=['blink', 'dark']))



def clear_screen():
    env = platform.system()
    if env is 'Windows':
        subprocess.call('cls', shell=True)

    if env is 'Linux':
        subprocess.call('clear', shell=True)

def usage():
    print(colored('''
    usage: python2 potoPort.py [-t] -[-h]
    -t, --target site/computer IP Address    
    -h, --help Help Menu
    
    ''', 'cyan'))

def get_parameters():
    global target
    parser = argparse.ArgumentParser(description="potoPort")
    parser.add_argument("-t", "--target", dest="target", help="site/computer IP Address")
    args = parser.parse_args()
    if args.target is not None:
        target = args.target
    else:
        usage()

def start():
    global total
    if len(sys.argv) > 1:
        clear_screen()
        print(colored(logo, 'cyan', attrs=['blink', 'dark']))
        get_parameters()
        t1 = datetime.now()
        print(colored('[+] Please wait connecting to IP...', 'green'))
        print(colored('[i] IP: ' + target, 'green'))
        print(colored('[+] Scanning port takes time..', 'cyan'))

        t2 = datetime.now()
        total = t2 - t1
        try:

            # for port1 in list(
            #         [22, 80, 443, 21, 100, 23, 1604, 0, 101, 102, 104, 8080, 1234, 1900, 123, 27960, 27015, 1024, 3072,
            #          27665, 65000, 27665, 1524, 1900, 19, 161, 27015, 17, 69, 3072, 1024, 27444, 31335, 27665, 1434,
            #          1, 5, 7, 18, 20, 29, 37, 42, 43, 49, 53, 69, 70, 79, 103, 109, 110, 115, 118, 119, 137, 139, 143,
            #          150, 156, 161, 179, 190, 194, 197, 396, 444, 4444, 445, 458, 546, 547, 563, 569, 1080, 3306, 44818,
            #          47001, 44405, 43594, 43595, 43110, 40000, 37008, 35357, 34197, 34000, 33848, 33434, 32976, 32887,
            #          32764, 32400, 32137, 31457, 31438, 31416, 31337, 30564, 29920, 29900, 29901, 29070, 29000, 28960,
            #          28910, 28852, 28785, 28786, 28770, 28771, 28015, 28001, 27960, 27969, 27950, 27901, 27910, 27888,
            #          27500, 27900, 27374, 27031, 27036, 27017, 27016, 27015, 27015, 27014, 27050, 27000, 27009, 27000,
            #          27000, 27006, 27000, 27001, 27002, 27003, 27004, 27005, 27006, 27007, 27008, 27009, 27010, 27030,
            #          26900, 26901, 26000, 26000, 26000, 25826, 25575, 25565, 25565, 24842, 24800, 24554, 24465, 443,
            #          444, 4444, 24444, 24441, 23513, 23399, 23073, 22222, 22136, 22000, 21025, 20808, 20595, 20560,
            #          20000, 19999, 19814, 19813, 19812, 19315, 19302, 19295, 19294, 19283, 19226, 19150, 19132, 19001,
            #          19000, 18606, 18605, 18506, 18505, 18401, 18400, 18333, 18306, 18301, 18300, 18206, 18201, 18200,
            #          18104, 18092, 18091, 17500, 17011, 16567, 16482, 16400, 16403, 16472, 16393, 16402, 16384, 16387,
            #          16384, 16387, 16384   ]):
            for port in range(0,64738):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((target, port))
                if result == 0:
                    print(colored("[+] Open Port {}".format(port), 'green'))
                #else:
                 #   print(colored("[X] Closed Port {}".format(port), 'magenta'))
            sock.close()
            sys.exit(colored('Scanned Completed : ' + str(total), 'green'))

        except KeyboardInterrupt:
            sys.exit(colored('[!] Ctrl + C Pressed', 'red'))

        except socket.gaierror:
            sys.exit(colored('[!] IP/Host couldnt resolved', 'red'))

        except socket.error:
            sys.exit(colored('[!] Unable to ping IP/Host', 'red'))

    else:
        usage()


if __name__ == '__main__':
    start()


