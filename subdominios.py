

import argparse
import requests
from os import path
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', help='Indica el dominio víctima')
parser = parser.parse_args()

def main():
    if parser.target:
        if path.exists('subdominios.txt'):
            wordlist = open('subdominios.txt', 'r')
            wordlist = wordlist.read().split('\n')
            
            for subdominio in wordlist:
                url = 'http://' + subdominio + '.' + parser.target
                try:
                    requests.get(url)
                except requests.ConnectionError:
                    pass
                else:
                    print ('(+) Subdominio descubierto: ' + url)
    else:
        print ('Por favor introduce un dominio válido')
        sys.exit()
    


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
