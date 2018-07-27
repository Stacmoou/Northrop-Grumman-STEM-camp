#Streams of Streams
#By Sarah L.
import random
import os
os.system('color 0a')
wordlist=["The","Matrix"]
wordlist.append(input("Enter a Word"))
while True:
    num=random.randint(33,254)
    index=random.randint(0,len(wordlist)-1)
    print(chr(num)+wordlist[index],end='')
