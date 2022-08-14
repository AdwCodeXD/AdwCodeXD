f = eval(input("Enter First Term: "))
d = eval(input("Enter Common Difference: "))



x2 = f + d
x3 = f + (2*d)
x4 = f + (3*d)
x5 = f + (4*d)



print ("First Five Terms = ",f,",",x2, ",",x3, ",",x4, ",",x5)


n = eval(input("Enter Postion: "))
x = f + (n-1) * d

print("nth Term = ",x)

Sn = n/2 * (f + x)

print("Sum of first n Terms = ", Sn)











