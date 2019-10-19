#Q1

def solve(numheads,numlegs):

    ns="no solutions"
    for i in range(numheads + 1):
        j = numheads - i
        if (2*i) + (4*j) == numlegs:
            return i,j
    return ns,ns

numheads = 35
numlegs = 94

solutions = solve(numheads,numlegs)
print(solutions)

#Q3
a = input("Enter your sentence! ")
print(a[::-1])

#Q4
#a = input("enter your string")
#list = [a]

#for alpha in list:


#dict = {}
#for

class Shape:
    def __init__(self,length,side):
        self.length = length
        self.side = side

    def area(self,length):
        area = length * length

    class square:
        def __init__(self,length):
            self.length = length

        def area(self, length):
            area2 = length * length

#Q6

def func(x,y):
    ry:
    	print(x/y)

    except ZeroDivisionError:
        print("you can't divide any value with zero")

    else:
        print(c)

a = func(5,0)

#Q7
a = "mansoor@gmail.com"
new = a.split("@")
print(new[0])

#Q8
