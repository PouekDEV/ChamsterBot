name = input("Give the name of the output file (can include .txt end) ")
import os
f = open(str(name),"w")
actualtext = input("What secret message do you want to code? ")
print("Coding")
actualtext = str(actualtext).replace("a","0")
actualtext = str(actualtext).replace("b","9")
actualtext = str(actualtext).replace("c","8")
actualtext = str(actualtext).replace("d","7")
actualtext = str(actualtext).replace("e","6")
actualtext = str(actualtext).replace("f","5")
actualtext = str(actualtext).replace("g","4")
actualtext = str(actualtext).replace("h","3")
actualtext = str(actualtext).replace("i","2")
actualtext = str(actualtext).replace("j","1")
actualtext = str(actualtext).replace("k","~")
actualtext = str(actualtext).replace("l","-")
actualtext = str(actualtext).replace("m","|")
actualtext = str(actualtext).replace("n","=")
actualtext = str(actualtext).replace("o","+")
actualtext = str(actualtext).replace("p","_")
actualtext = str(actualtext).replace("r","'")
actualtext = str(actualtext).replace("s","/")
actualtext = str(actualtext).replace("t","`")
actualtext = str(actualtext).replace("u","*")
actualtext = str(actualtext).replace("w","(")
actualtext = str(actualtext).replace("y",")")
actualtext = str(actualtext).replace("x","&")
actualtext = str(actualtext).replace("z","^")
actualtext = str(actualtext).replace("q","$")
f = open(str(name),"w")
f.write(actualtext)
f.close()
print("Message coded")
os.system("menucoder.py")