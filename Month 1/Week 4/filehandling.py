# open and close file
# default mode is read
f = open("demo.txt")
print(f.read())
print("-----------------------------")
f.close()


# return one line by using the readline() method
with open("demo.txt") as f:
  print(f.readline())

# append mode 
with open("demo.txt", "a") as f:
    f.write("\nAppended Text!!!\n")
with open("demo.txt") as f:
    print(f.read())

# write mode. it will overwrite any existing content
with open("demo.txt","w") as f:
   f.write("Overwrite text!!")
with open("demo.txt") as f:
    print(f.read())

import os
# create mode
if os.path.exists("new.txt") == False:
    f = open("new.txt" , "x")
    f.close()
with open("new.txt", "a") as f:
    f.write("\nAppended Text!!!\n")
with open("new.txt") as f:
    print(f.read())

# Delete file
os.remove("new.txt")
print("File deleted successfully!!!")