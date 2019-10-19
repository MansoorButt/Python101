def bitwise(m,n):  # m = 5 , n= 8
# x is a variable here
    x=m+1  # x = 6
    ops = m
    while True:  # this loop will work till the 'if' condition in NOT true !
         # m=5 , x= 6
        ops = ops ^ x
        x = x+1
        if(x>n):  
            break
    return ops

y = bitwise(5,8)

print(y)

