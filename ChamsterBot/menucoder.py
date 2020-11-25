import os
print("code")
print("decode")
print("exit")
mode = input("What do you want to do? ")
if str(mode) == "code":
    os.system("coder.py")
if str(mode) == "decode":
    os.system("decoder.py")
if str(mode) == "exit":
    os.system("main.py")