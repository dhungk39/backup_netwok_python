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

################################		
f1 = open("file1", "r")
f2 = open("file2", "r")

i = 0

for line1 in f1:
	i += 1
	
	for line2 in f2:
		
		# matching line1 from both files
		if line1 == line2:
			# print IDENTICAL if similar
			print("Line ", i, ": IDENTICAL")	
		else:
			print("Line ", i, ":")
			# else print that line from both files
			print("\tFile 1:", line1, end='')
			print("\tFile 2:", line2, end='')
		break

# closing files
f1.close()									
f2.close()			
