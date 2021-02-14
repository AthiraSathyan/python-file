import arithemetic.add
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("sum=",arithemetic.add.add(a,b))
from arithemetic.sub import sub
print("difference=",sub(a,b))
from arithemetic.carithemetic.mul import *
from arithemetic.carithemetic.div import div as d
print("product=",mul(a,b))
print("quoitent=",d(a,b))
