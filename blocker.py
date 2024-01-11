#!/usr/bin/python3
import time
import platform
from datetime import datetime as dt

from ip_addresses import ip_addresses
from web_to_be_blocked import web_list

host_temp = "/etc/hosts"
# redirect = ip_addresses

while True:
    if (dt(dt.now().year, dt.now().month, dt.now().day, 8, 59) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 5, 59)):
        print("Working Hours....")
        with open(host_temp, mode='r+', encoding='utf-8') as f:
            content = f.read()
            # print(content)
            for website in web_list:
                if website in content:
                    # print(content)
                    pass
                else:
                    for ip_address in ip_addresses:
                        # redirect = ip_address
                        f.write(ip_address + "\t" + website + "\n")
    else:
        with open(host_temp, mode='r+', encoding='utf-8') as f:
            content = f.readlines()
            f.seek(0)
            for line in content:
                if not any(website in line for website in web_list):
                    f.write(line)
            f.truncate()
        print("Fun hours...")
        
    time.sleep(5)