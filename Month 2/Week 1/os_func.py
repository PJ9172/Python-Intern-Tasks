""""
Python has a built-in os module with methods for interacting with the operating system, 
like creating files and directories, management of files and directories, 
input, output, environment variables, process management, etc.
"""

import os

print(os.getcwd())          # current directory

print(os.listdir())         # list files

print (os.getenv("HOME"))   # return env variable value


# Creating new dir , changing dir , removing dir.

print("Current directory:" , os.getcwd())
# Create a new directory
print("Creating new dir!!")
os.mkdir("mydir")
os.chdir("mydir")
print("Current directory now:" , os.getcwd())
os.chdir("D:\Prajwal\Python Tasks\Month 2\Week 1")
# Removing new created dir
print("Removing mydir dir!!")
os.rmdir("mydir")
print("Current directory now:" , os.getcwd())
