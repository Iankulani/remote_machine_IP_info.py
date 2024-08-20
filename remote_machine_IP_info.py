# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 20:01:51 2024

@author: IAN CARTER KULANI
Email_address:iancarterkulani@gmail.com
phone number:+265(0)988061969
Purpuse: To get remote machine internet protocal address 
Usage: The program will prompt you to enter the remote host and then display its IP address. 

"""

#!/usr/bin/env python
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.
import socket
def get_remote_machine_IP_info():
    remote_host = input("Enter the remote host:")
    try:
      print ("IP address of %s: %s" %(remote_host,
     socket.gethostbyname(remote_host)))
    except socket.error as err_msg:
      print ("%s: %s" %(remote_host, err_msg))
if __name__ == '__main__':
    get_remote_machine_IP_info()