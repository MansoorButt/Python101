for i in range(1,2019,1):
    if i % 5 == 0 and i % 7 == 0 and i % 15 != 0:
        print(i,sep=",")


attempts = 0
number = 5

while(attempts!= 3):
    guess=input("enter your Number from 1-10")
    
