
#!/usr/bin/env python3

import socket
import sys

def banner (ip, port):
    s = socket.socket()
    s.connect((ip, port))
    print (str(s.recv(1024)))

def main():
    ip  =  input('Introduce la IP del objetivo: ') #'192.168.1.89'
    port = int(input('Introduce el puerto a escanear: ')) # 22
    banner(ip, port)
    


if  __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
    