#File Exception

a= 20
b = 0

try:
	print(a/b)

except ZeroDivisionError:
    print("you can't divide any value with zero")

else:
    print(c)

# Using 2 or more than 2 Exceptions by grouping them to display the error !
c = 6
d = 6
g =[]

try :
    e = c/d
    f = g[5]

except (ZeroDivisionError , IndexError):
    print("Handle ZeroDivisionError or IndexError")

else:
    print(e)


#TASK
x = "Mansoor"
y= 5

try:
    z =x/y


except Exception as f:
    print("Error" + str(e))
