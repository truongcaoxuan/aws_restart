# Lab 15: Introducing System Administration with Python

# Using os.system
import os
os.system("ls")

# Using subprocess.run
""" full list of arguments for subprocess.run() looks like the following list:

subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, 
               check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None) 
"""
import subprocess
subprocess.run(["ls"])

# Using subprocess.run with two arguments
subprocess.run(["ls","-l"])

# Using subprocess.run with three arguments
subprocess.run(["ls","-l","README.md"])

# Retrieving system information
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

# Retrieving information about disk space
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

