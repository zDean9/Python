#Website Blocker# 


import time 
from datetime import datetime as dt 
hosts_path = r  # r is for raw string 
hosts_temp = "hosts"
redirect = "127.0.0.1"
web_sites_lists = ["www.facebook.com", "facebook.com"] #users can modify lists of websites they want to block

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,22):
        print("Working hours")
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in content:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
        
    else:
        print("Fun time")
        with open(hosts_path, "r+") as file:
            content = file.read.lines()
            file.seek(0) #reset the pointer tp the top of the text file
            
            for line in content:
                if not any('www.facebook.com'):
                    file.write(line)
                    file.truncate
                    time.sleep(5)
