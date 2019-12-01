#!/usr/bin/python3

import socket
from termcolor import colored


def retBanner(host, port):
    try:
        socket.setdefaulttimeout(2)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        banner = sock.recv(1024)

        return banner
    except:
        return


def main():
    host = str(input(colored("[*] Enter the target IP: ", 'blue')))
    p = int(input(colored('[*] Enter the port upper bound: ', 'blue')))
    for i in range(1, p+1):
        banner = retBanner(host, i)

        if banner:
            print(colored(f"[+] {host}:{i}  ->     " + banner.decode("utf-8"), 'green'), end='')
        else:
            print(colored(f"[-] {host}:{i}  ->     " + "Unable to Detect", 'red'))

    exit(0)


main()
