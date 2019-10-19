a,b = 1,2
b,a = a,b
print(a,b)

if a % 2 == 0 :
    c = 2
else:
    c = 3

myList = [
(1,2,3),
(5,9,8),
(2,4,6)]

b= []
b = myList[1]
myList[1]=myList[2]
myList[2]=b

print(myList)



new_dict = {"num":"5","num2":"3", "num3":"4"}

for keys in new_dict:
    if new_dict[keys] > new_dict[keys + 1]:
        new_dict[keys+1]

for i in range(1,2019):
    if i % 5 == 0 and i % 7 == 0 and i % 15 != 0
    print(i,sep=",")

