from random import *

elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
try:
    length = int(input(": "))
except ValueError:
    print("Error:", ValueError)

pasword = ""

for i in range(length):
    pasword += choice(elements)
print(pasword)