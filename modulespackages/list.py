from listop2 import *
a=input("enter list:")
l=a.split()
l=[int(i) for i in l]
print("List:",l)
print("Uniquelist:")
unique(l)
print("Square of list:")
square(l)
