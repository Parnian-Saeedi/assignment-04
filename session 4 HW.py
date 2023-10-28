import random

pcnumber= random.randint(0,100)
count=0
while True:
    usernumber = int(input("enter a number:"))
    count+=1
    if usernumber == pcnumber:
        print("welldone!")
        break
    if usernumber > pcnumber:
            print("guess smaller number")
    if pcnumber>usernumber:
        print("guess bigger number")
print(pcnumber)
print(count) 