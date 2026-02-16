import math
x1 = input("Enter x1: ")
y1 = input("Enter y1: ")
r = input("Enter radius: ")
x2 = input("Enter x2: ")
y2 = input("Enter y2: ")
n1 = math.pow(int(r),2)
n2 = math.pow((int(x1) - int(x2)),2)
n3 = math.pow((int(y1) - int(y2)),2)
n4 = n2+n3
bb3 = n1 > n4
print (bb3)