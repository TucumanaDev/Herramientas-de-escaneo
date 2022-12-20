#!/usr/bin/python3
#coding: utf-8

import os
import re, sys, subprocess

if len(sys.argv) !=2: 
   print("\n[!] Uso: python3 " + sys.argv[0] + " <dirección IP>\n")
   sys.exit(1)

def get_ttl(ip_addres):
    proc = subprocess.Popen(["/usr/bin/ping -c 1 {}".format(ip_addres), ""], stdout=subprocess.PIPE, shell= True)
    (out,err) = proc.communicate()
    out = out.split()
    out = out[12].decode('utf-8')
    ttl_value=re.findall(r"\d{1,3}", out)[0]
    
    return ttl_value

def get_os(ttl):
    ttl = int(ttl)

    if ttl > 0 and ttl <= 64:
        return "Linux"

    elif ttl > 65 and ttl <= 128:
        return "Windows"
    
    else:
        return "Not found"

if _name_ == "_main_":

    ip_format = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
    ip_addres = sys.argv[1]

    try:
        if ip_addres == ip_format:
            print("\n[!] Uso: python3 " + sys.argv[0] + " <dirección IP (000.000.000.000)>\n")
            sys.exit(1)    
    except IndexError:
        pass

    ttl = get_ttl(ip_addres)

    os_name = get_os(ttl)

    print("{} (ttl:{}) = {}".format(ip_addres, ttl, os_name))