
from random import *


chipotle_list = [["beans","brown rice","white rice"],["cheese","sour cream","mild"],
["green sauce","red sauce","meat"]]

x = randint(0, len(chipotle_list)-1)
y = randint(0, len(chipotle_list)-1)

print(chipotle_list[x][y])
