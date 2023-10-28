import random
while True:
    a= input("play or exit: ")
    if a == "exit":
        break

    if a == "play":
        dicenumber= random.randint(1,6)
        if dicenumber == 1 or 2 or 3 or 4 or 5:
            print(dicenumber)
        if dicenumber == 6:
            print("luckyy,throw the dice again")
            dicenumber = random.randint(1,6)
            print(dicenumber)
            break
    
    
