import string
import random

allchar=string.printable
listchar=list(allchar)
password=input("Enter Password : ")

guespass=""

while (guespass!=password):
    
    guesspassword=random.choices(listchar,k=len(password))
    print(f'===========>{str(guesspassword)}=============>')
    
    
    if (guesspassword==list(password)):
        print("password is : " + guespass.join(guesspassword))
        break