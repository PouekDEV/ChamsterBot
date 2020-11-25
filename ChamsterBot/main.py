print("  /$$$$$$  /$$                                           /$$                               /$$$$$$$              /$$                      ")
print(" /$$__  $$| $$                                          | $$                              | $$__  $$            | $$              ")
print("| $$  \__/| $$$$$$$   /$$$$$$  /$$$$$$/$$$$   /$$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$       | $$  \ $$  /$$$$$$  /$$$$$$        ")
print("| $$      | $$__  $$ |____  $$| $$_  $$_  $$ /$$_____/|_  $$_/   /$$__  $$ /$$__  $$      | $$$$$$$  /$$__  $$|_  $$_/       ")
print("| $$      | $$  \ $$  /$$$$$$$| $$ \ $$ \ $$|  $$$$$$   | $$    | $$$$$$$$| $$  \__/      | $$__  $$| $$  \ $$  | $$           ")
print("| $$    $$| $$  | $$ /$$__  $$| $$ | $$ | $$ \____  $$  | $$ /$$| $$_____/| $$            | $$  \ $$| $$  | $$  | $$ /$$        ")
print("|  $$$$$$/| $$  | $$|  $$$$$$$| $$ | $$ | $$ /$$$$$$$/  |  $$$$/|  $$$$$$$| $$            | $$$$$$$/|  $$$$$$/  |  $$$$/         ")
print(" \______/ |__/  |__/ \_______/|__/ |__/ |__/|_______/    \___/   \_______/|__/            |_______/  \______/    \___/    ")
print("V.0.3")
import os
from os import system, name 
from time import sleep
print("'search'")
print("'ascii'")
print("'yt'")
print("'code'")
print("'license'")
mode = input("What do you want to do?")
if str(mode) == "search":
    os.system("search.py")
if str(mode) == "ascii":
    os.system("ascii.py")
if str(mode) == "yt":
    os.system("yt.py")
if str(mode) == "code":
    os.system("menucoder.py")
if str(mode) == "license":
    os.system("license.py")
# Comments
# python -m py_compile main.py