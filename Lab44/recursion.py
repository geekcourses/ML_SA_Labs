# Recursive Acronim:GNU = GNU isNot Unix

# Recurcive Function

# 3! = 3*2*1 = 6
# if n>1: fact(n)= n*fact(n-1)
# n=1   : fact(1)=1

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)


print( fact(1) )
print( fact(5) )
print( fact(3) )

