nmap a.k.a Network Mapper is an industry-standard network scanner which sends packets & analyses the responses. 
This in turn enables a user to discover hosts & services connected to a specific computer network.

In this document, I will run you through how I created a port scanner inspired by nmap. 

A port scanner allows us to find open ports that exist on a server.
The scanner works for both web apps in addition to remote host. The tool provides the basic functionality of a port scanner. 
The functionality works through the use of Sockets.
The imported libraries are socket and pyfiglet (not necessary, but exists for aesthetic purposes). 

There is three criteria which our port scanner must fulfil.

1. Allows us to specifiy the target (we can accomplish this by storing the target as a variable)
2. Make requests to all ports 
3. Return every open port (accomplished using Sockets)

# Source code:

First we will import our libraries.
  
    import pyfiglet
    import sys
    import socket
    from datetime import datetime

Pyfiglet allows us to create our cute banner at the top.

System enables us to handle exceptions.

Socket facilitates network communication, enabling the functionality of this port scanner.

Datetime allows us to print the date and time for our banner and as an output.

# Create a banner

    ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
    
    print(ascii_banner)

This prints a banner at the top of the script.

# Defining a target
	
      target = input(str("Target's IP address: "))

The target variable creates an input for the user to enter the target's IP address.

I have forced the IP address to be a string throughout the rest of the script to ensure there are no errors.

# Add Banner 
    print("-" * 50)
    print("Scanning Target: " + target)
    print("Scanning started at:" + str(datetime.now()))
    print("-" * 50)

This prints a line above and below the information about the scan (for aesthetic purposes), where the target and what date & time the scan began.

# Detecting all open ports on the server

    try:
	
	    for port in range(1,65535):
		    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		    socket.setdefaulttimeout(1)

This part of the script begins scanning all ports within the valid port range on all systems.

Then, we create a variable 's' and turn it into a socket, which has a default time out of 1 second. This will be how long it waits before skipping that port and moving on to the next port.
      
		  result = s.connect_ex((target,port))
    
		  if result == 0:
			  print("Port {} is open".format(port))
		  s.close()

A successful connection is indicated by the result of the socket being 0.

This prints a string saying which port is open.

Then, it closes the socket and moves on to the next port.
		
    except KeyboardInterrupt:
    		print("\n Exiting...")
    		sys.exit()
    except socket.gaierror:
    		print("\n Hostname could not be resolved!")
    		sys.exit()
    except socket.error:
    		print("\ Server not responding!")
    		sys.exit()

Here, we catch: 
1. Keyboard interrupts
2. DNS errors
3. Errors connecting to host address (essentially any other error the socket library comes into contact with)

# That's the basics!

# In order to improve functionality...

There are two main ways in which I can improve upon this program.
1. Create a list of common protocols, and return the protocol that matches the port number. (e.g. SSH - 22)
2. Use threading to increase the speed at which the port scanner scans.

I may come back to these and include the code to action both these improvements.

# WARNING! 
Using a port scanner is akin to 'urching' a.k.a trying to open (un)locked car doors at night!
If you use this tool against an entity, your ISP may contact you.

You have been warned.

Happy scanning!
