print("  /$$$$$$  /$$                                           /$$                               /$$$$$$$              /$$                       /$$$$$$       /$$  ")
print(" /$$__  $$| $$                                          | $$                              | $$__  $$            | $$                      /$$$_  $$    /$$$$ ")
print("| $$  \__/| $$$$$$$   /$$$$$$  /$$$$$$/$$$$   /$$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$       | $$  \ $$  /$$$$$$  /$$$$$$         /$$    /$$| $$$$\ $$   |_  $$  ")
print("| $$      | $$__  $$ |____  $$| $$_  $$_  $$ /$$_____/|_  $$_/   /$$__  $$ /$$__  $$      | $$$$$$$  /$$__  $$|_  $$_/        |  $$  /$$/| $$ $$ $$     | $$  ")
print("| $$      | $$  \ $$  /$$$$$$$| $$ \ $$ \ $$|  $$$$$$   | $$    | $$$$$$$$| $$  \__/      | $$__  $$| $$  \ $$  | $$           \  $$/$$/ | $$\ $$$$     | $$  ")
print("| $$    $$| $$  | $$ /$$__  $$| $$ | $$ | $$ \____  $$  | $$ /$$| $$_____/| $$            | $$  \ $$| $$  | $$  | $$ /$$        \  $$$/  | $$ \ $$$     | $$  ")
print("|  $$$$$$/| $$  | $$|  $$$$$$$| $$ | $$ | $$ /$$$$$$$/  |  $$$$/|  $$$$$$$| $$            | $$$$$$$/|  $$$$$$/  |  $$$$/         \  $//$$|  $$$$$$//$$ /$$$$$$")
print(" \______/ |__/  |__/ \_______/|__/ |__/ |__/|_______/    \___/   \_______/|__/            |_______/  \______/    \___/            \_/|__/ \______/|__/|______/")
import os
from os import system, name 
from time import sleep
query = input("Enter words to search:")
str(query)
hm = input("How many results do you want?:")
int(hm)
ts = input("How long I can search for you?:")
int(ts)
jezyk = input("Which language do you prefer?(type en or pl or other language):")
str(jezyk)
_ = system('cls')
print("  q-p")
print(' /\"/\"')
print("(`=*=')")
print(" ^---^`-._")
print("Searching...")
try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
# to search 
  
for j in search(query, tld="co.in", lang=str(jezyk), num=int(hm), stop=int(hm), pause=int(ts)):
    print(j) 
sleep(2) 
want = input("Do you want to search again(yes/no)?")
str(want)
if str(want) == "yes":
    print("Browsing bo brrrr")
    os.system("main.py")
if str(want) == "no":
    print("*smirk* goodbye!")

# Comments
# python -m py_compile main.py