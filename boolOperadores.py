name = "andres"
age = 27

print(name == 'andres' or age == 27)
print(name == 'andres' and age != 23)

name2 = 'luis'
edad = 17

b1 = name2 == 'elsa' or not edad > 17
print (b1)

b2 = name2 == 'elsa' or not (name == 'luis' and edad == 17)
print (b2)
