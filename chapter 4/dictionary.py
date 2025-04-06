# info = {
#     "name": ["kaddu","karela"],
#     "learning": "python",
#     "age": [19, 21]
# }

# print(info["name"][1])
# print(info["learning"])
# print(info["age"])

# print(type(info))

# info["name"] = "mannusahilu"
# info["surname"] = "pantbajaj"  # they both are use to update dict
# print(info)

# info.update({"sal": 12})
# print(info)

# null_dict ={}
# null_dict["name"]="sahilmegha"
# print(null_dict)


# Nested dictionary:
student = {
    "name": "megha",
    "namee": "sahil",
    "subj": {
        "phy" : 78,
        "chem":66,
        "math":99}
}
# print("marks in phy: " + str(student["subj"]["phy"]))
# print(student["subj"]["chem"])
# print(student["subj"]["math"])

# method:
print(len(student))
print(list(student.keys()))
print(list(student["subj"].keys()))
print(list(student.values()))
print(list(student["subj"].values()))
print(student.items())


 
