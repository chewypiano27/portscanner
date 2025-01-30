import pyfiglet
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("CHEWYPIANO27 PORT SCANNER")
print(ascii_banner)

# Defines a target
target = input(str("Target's IP address: "))
# Adds the banner 
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)

try:
	
	# Scans all possible ports within the range
	for port in range(1,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		
		# Error indicator
		result = s.connect_ex((target,port))
		if result ==0:
			print("Port {} is open".format(port))
		s.close()
		
except KeyboardInterrupt:
		print("\n Goodbye.")
		sys.exit()
except socket.gaierror:
		print("\n Hostname Could Not Be Resolved!")
		sys.exit()
except socket.error:
		print("\ Server not responding!")
		sys.exit()
