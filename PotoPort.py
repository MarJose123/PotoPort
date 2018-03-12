#-- coding: utf8 --
#!/usr/bin/python
import sys, os, logging
import platform, time
import socket
import argparse
from termcolor import colored
from datetime import datetime





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
        os.system('cls')

    if env is 'Linux':
        os.system('clear')

    else:
        print(colored('Unable to Clear Screen', 'red'))

def usage():
    print(colored('''
    usage: python2 potoPort.py [-t] -[-h] [-v]
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
    if len(sys.argv) > 1:
        get_parameters()
        global total
        t1 = datetime.now()
        print(colored('Please wait connecting to IP...', 'green'))
        print(colored('IP: ' + target, 'green'))

        t2 = datetime.now()
        total = t2 - t1
        try:
            ##62000
            for port in list(
                    [22, 80, 443, 21, 100, 23, 1604, 0, 101, 102, 104, 8080, 1234, 1900, 123, 27960, 27015, 1024, 3072,
                     27665, 65000, 27665, 1524, 1900, 19, 161, 27015, 17, 69, 3072, 1024, 27444, 31335, 27665, 1434,
                     1, 5, 7, 18, 20, 29, 37, 42, 43, 49, 53, 69, 70, 79, 103, 109, 110, 115, 118, 119, 137, 139, 143,
                     150, 156, 161, 179, 190, 194, 197, 396, 444, 4444, 445, 458, 546, 547, 563, 569, 1080, 3306]):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((target, port))
                if result == 0:
                    print(colored("Open Port {}".format(port), 'green'))
                sock.close()


        except KeyboardInterrupt:
            sys.exit(colored('Ctrl + C Pressed', 'red'))

        except socket.gaierror:
            sys.exit(colored('IP/Host couldnt resolved', 'red'))

        except socket.error:
            sys.exit(colored('Unable to ping IP/Host', 'red'))
    else:
        usage()


if __name__ == '__main__':
    start()
    sys.exit(colored('Scanned Completed : ' + str(total), 'green'))

