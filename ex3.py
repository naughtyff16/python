import re

str5= "IT IS VERY COLD TODAY HERE"

mat1=re.search("\s",str5)

print(mat1)

print("the first space is available at",mat1.start())
