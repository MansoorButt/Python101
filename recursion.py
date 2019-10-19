#Factorial Function

def fact(n):
    if n == 0:
        return 1

    else:
        return (n*fact(n-1))
2
number = int(input("enter a number:"))
print("Factorial is",fact(number))

#5!= 5 x 4 x 3 x 2 x 1
