import time
from datetime import datetime as dt # to avoid having to do datetime.datetime
# if import datatime as dt, then it would be only dt.datetime

hosts_temp = 'hosts'

# using the r allows us to escape escape characters
hosts_path = '/private/etc/hosts'
redirect = '127.0.0.1'

sites_that_kill_me = ['www.facebook.com', 'facebook.com', 'www.twitter.com', 'twitter.com', 'www.instagram.com', 'www.youtube.com']

print(dt.now())

while True:
    # create 3 datatime objects and compare them
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print('Working Hours: ')
     # load, read and write to the hosts file, using the r+ allows reading and writing to the file
        with open(hosts_path, 'r+') as file:
            content = file.read() # this will load the entire file
            for site in sites_that_kill_me:
                if site in content:
                    pass
                else:
                    file.write(redirect+' '+site+'\n')
    else:
        with open(hosts_path, 'r+') as file:
    # readlines method will produce a list with each str item
    # then check the realines list against the sites that kill me list, and if items them I want them out, but no method to delete but append yes
            content = file.readlines()
    # once readline is complete the pinter will be sitting at the very end of the file
    # so any append method will add from the point of the pointer
    # the seek method will place pointer where we want
            file.seek(0)
            for line in content:
    # if item not there, append a new file hosts via writing a new file
                if not any(site in line for site in sites_that_kill_me):
                    file.write(line)
    # trucate methond will delete all things UNDER the specified section
                file.truncate()
            print('time to play!!!')
        time.sleep(600)
