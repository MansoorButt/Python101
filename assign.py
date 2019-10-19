employee = [["Ali","khan","teacher"],["mansoor","butt","Ai develepor"],["Waqas","ahmed","manager"]]

name = []

for i in employee :
    name.append(i[0])

print(name)

#List Comprehension

l6 = [i[0] for i in employee]
print(l6)

idCard = {
   "name" : "Ali",
   "rollno" : "111045",
   "nationality" : "Pakistani"

}


#print(idCard.rollno)


# Function

def Add(x,y):

    return x + y

math = Add(50,40)
print(math)
