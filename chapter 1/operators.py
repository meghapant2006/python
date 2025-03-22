# Arithmetic operators
# +, -, *, /, %, **, //

a=5
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b) #5^2
print(a//b) #5/2=2.5


# Relational / Comparison operators
# ==, !=, >, <, >=, <=

a=50
b=10
print(a==b) #False
print(a!=b) #True
print(a>b)  #True
print(a<b)  #False
print(a>=b) #True
print(a<=b) #False


# Assignment operators
# =, +=, -=, *=, /=, %=, **=, //=

num = 10
num = num+10
num += 10   
num -= 10
num *= 10 
num /= 10 
num %= 10
num **= 10
num //= 10 
print("num:", num)
 

# Logical operators
# not, and, or

a=50
b=30
print(not True)
print(not False)
print(not (a>b))

value1= True
value2 =False
print("AND operator :" , value1 and value2) 

print("OR operator :" , value1 or value2) 
print("OR operator :" , (a==b) or (a>b))
