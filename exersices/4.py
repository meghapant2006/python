# dict ={
#     "table": ['a piece of furniture ', 'list of facts and figure'],
#     "cat" :"a small animal"
# }
# print(dict)



# subjects = {"python", "java", "C++", "python",
#             "js", "java", "python", "java", "C++", "C"}
# num = len(subjects)
# print(f"There are {num} of class room")

# print("okok:",num)
# print(f"ok {num} ok")  example



marks = {}
x = int(input("enter phy: "))
marks.update({"phy": x})

y = int(input("enter math: "))
marks.update({"math": y})

z = int(input("enter eng: ")) 
marks.update({"eng": z})

print(marks)
