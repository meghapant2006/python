# # if-elif-else
# if(condition):
#     statement
# elif(condition):
#     statement
# else:
#     statement


# age = int(input("user age is:"))
# if (age >= 18):
#     print("can vote and apply for license")
# elif (age == 16):
#     print("the person can apply for license but not for voter ")
# else:
#     print("can't vote")
#  if for start condition
#     elif for beach ke sare cheej aur elif kitne bhi aa sakte hai
# else for end

# light=str(input("light color is:"))
# if(light=="red"):
#     print("stop")
# elif(light=="green"):
#     print("go")
# elif(light=="yellow"):
#     print("ready")
# else:
#     print("abe andhheee")

# Write a program to input a student's marks and print their grade using the following conditions:
# Marks >= 90 → Grade A
# Marks >= 80 → Grade B
# Marks >= 70 → Grade C
# Marks >= 60 → Grade D
# Marks < 60 → Grade F

# marks=int(input("marks of student is:"))
# if(marks>=90):
#     print("A grade")
# elif(marks>=80):
#     print("B grade")
# elif(marks>=70):
#     print("C grade")
# elif(marks>=60):
#     print("D grade")
# elif(marks>=50):
#     print("E grade")
# else:
#     print("Fail")


# marks=int(input("marks of student is:"))
# if(marks>=90):
#     print("A grade")
# elif(marks>=80 and marks<90) :
#     print("B grade")
# elif(marks>=70 and marks<80) :
#     print("C grade")
# elif(marks>=60 and marks<70) :
#     print("D grade")
# elif(marks>=50 and marks<60) :
#     print("E grade")
# else:
#     print("fail")


# nesting
age = 34
if (age >= 18):
    if (age >= 80):
        print("can't drive")
    else:
        print("can drive")

else:
    print("can't drive")


# age=int(input())
#     if(age>=18):
#         if (age>=60):
#             print()
#          else:
#             statement
#     else:
