#!/usr/bin/python3
import time
import platform
from datetime import datetime as dt

from ip_addresses import ip_addresses
from web_to_be_blocked import web_list

host_temp = "hosts"
# redirect = ip_addresses

while True:
    if (dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 22)):
        print("Working Hours.....")
        with open(host_temp, 'r+') as f:
            content = f.read()
            print(content)
            for website in web_list:
                if website in content:
                    pass
                else:
                    for ip_address in ip_addresses:
                        # redirect = ip_address
                        f.write(ip_address + "\t" + website + "\n")
    else:
        print("Fun hours...")
        
    time.sleep(5)