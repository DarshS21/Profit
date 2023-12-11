import os
import datetime
import socket
import subprocess

# Current date and timestamp
now = datetime.datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

# IP address of the computer
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

# The information in a text file
file_path = "C:\\temp\\hacked.txt"

with open(file_path, "w") as file:
    file.write(f"Date and Time: {timestamp}\n")
    file.write(f"IP Address: {ip_address}\n")
    file.write("Phrase: hacked\n")

# Ping the flemingcollege.ca website
subprocess.run(["ping", "flemingcollege.ca"])