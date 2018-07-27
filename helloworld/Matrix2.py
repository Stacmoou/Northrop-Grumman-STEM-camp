#Streams of Streams
#By Sarah L.
import random
import os
os.system('color 0a')
wordlist=["If","Class", "Module",'pygame', 'arcade', 'while', 'list', 'for', 'sprite', 'dunderscore', 'def', 'import', 'logic', 'conditonal', 'IDE', 'tinker', 'break', 'build', 'create']

while True:
    num=random.randint(33,254)
    index=random.randint(0,len(wordlist)-1)
    print(chr(num)+wordlist[index],end='')
