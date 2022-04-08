# Imports
import socket
import time
# Weclome Text
user_name = input('What is your name:')
print('Weclome ' + user_name) 
time.sleep(1)
addrs = input('What is the host names URL:')
time.sleep(1)
print('The IP of said host is ' + socket.gethostbyname(addrs))
time.sleep(1)
print('GoodBye!')