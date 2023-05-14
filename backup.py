import filecmp
from re import A
from netmiko import ConnectHandler
from datetime import date
import os
import time
import datetime
import json
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()           
drive = GoogleDrive(gauth)
import shutil

today = date.today()
directory = str(today) + "_Backup_Switch"
#//"< The path contain the backup file >"
parent_dir = "/Users/hung.nguyen4/Desktop/python_network"
path = os.path.join(parent_dir, directory)
os.mkdir(path)
print(path)

#//"< The path contain the imformation switch file host name switch and IP SSH switch >"
device_list = '/Users/hung.nguyen4/Desktop/python_network/switch.json'
with open(device_list) as json_file:
    data = json.load(json_file)
    for switch in data['switch_list']:
        switch_list = {
            'device_type':  'cisco_ios',
            'host': switch['ip'],
            'username': switch['username'],
            'port': switch['port'],
            'password': switch['password'],
            'secret':   switch['secret'],
    }
        try:
            net_connect = ConnectHandler(**switch_list)
        except:
            continue
        net_connect.enable()
        print("\n Initiating config backup")
        output2 = net_connect.send_command("show running-config")
        print(output2)
        SAVE_FILE  = open(path + "/" + str(today) + "_"+ switch['ip'] +"_"+ switch['hostname'] + ".txt","w")
        SAVE_FILE.write(output2)
        SAVE_FILE.close()
        print("\n Finished config backup")
print("\n Disconnect session")
net_connect.disconnect()

shutil.make_archive(path,"zip","/Users/hung.nguyen4/Desktop/python_network")
