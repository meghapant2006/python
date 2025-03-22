# variables  or values:-

name = "megha"
age = 18
weight = 39.5
print("my name is :", name)
print("my age is :", age)
print("my weight is :", weight)

print(type(name))
print(type(age))
print(type(weight))

name1 = "megha"
name2 = 'megha'
name3 = '''megha'''
print(name1)
print(name2)
print(name3)

age = 18
old = False
a = None
print(type(old))
print(type(a))

# print sum:-
a = 100
b = 200
sum = a+b
print(sum)

# print diff:-
a = 200
b = 100
diff = a-b
print(diff)

# Expressions Execution:-
a, b = 2, 3
txt = "@"
print(2*txt*3)
# concatination-
a, b = "2", 3
txt = "@"
print((a+txt)*b)
# arithmetic- bodmas
a, b = 2, 3
c = 4
print(a+b*c)
# multiplication of float and int is always a float
a, b = 10, 5.0
c = a*b
print(c)
# result of division of two number is always a float
a, b = 1, 2
c = a/b
print(c)
# division of float and int result is int but display as float
# integer division
a, b = 1.5, 3
c = a//b
print(c, a/b)

a, b = 12, 5
c = a//b
print(c)

a, b = -12, 5
c = a//b
print(c)

a, b = 12, -5
c = a//b
print(c)
# remainder is nagative when denominater is negative
a, b = -5, 2
c = a % b
print(c)

a, b = 5, 2
c = a % b
print(c)

a, b = 5, -2
c = a % b
print(c)
# taking input from user & printing it ...
name = input("name :")
age = int(input("age"))
weight = float(input("weight :"))
print(("My name is", name, "i am", age, "my weight is", weight))
