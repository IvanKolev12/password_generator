import string
import time
from random import *


print("<=====================================================>")
while True:
    resp = input("""\nPlease enter the type of password:
                    1)Password with letters
                    2)Password with digits
                    3)Password with characters
                    4)Mixed Password\n""""\n"
                 "[*] Enter valid option: ")
    
    if resp > '4':
        print('[!] This option is not correct!')
        break
    
    time.sleep(2)
    print('[*] You have selected option:',resp)
    time.sleep(3)
    print('[*] Generating password ...')

    if resp == '1':
        letcharacters = string.ascii_letters
        password = "".join(choice(letcharacters) for x in range(randint(8,32)))
        time.sleep(10)
        print("<=====================================================>")
        print("[+] Password created:" + password)
        print("<=====================================================>")

        
    elif resp == '2':
        digcharacters = string.digits
        password = "".join(choice(digcharacters) for x in range(randint(8,32)))
        time.sleep(10)
        print("<=====================================================>")
        print("[+] Password created:" + password)
        print("<=====================================================>")

        
    elif resp == '3':
        puncharacters = string.punctuation
        password = "".join(choice(puncharacters) for x in range(randint(8,32)))
        time.sleep(10)
        print("<=====================================================>")
        print("[+] Password created:" + password)
        print("<=====================================================>")


    elif resp == '4':
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(choice(characters) for x in range(randint(8,32)))
        time.sleep(10)
        print("<=====================================================>")
        print("[+] Password created:" + password)
        print("<=====================================================>")

        
