# Dictionary and Tuple

# Tuple
# Ordered Immutable Collection of Elements
Score = (1, 2, 3, 4, 5, 6)
friends = ("Anshika", "Rahul", "Rohan", "Robin", "Tahseenul", "Shomopriyo")

# Access Elements
print(friends)
print(friends[2])

# Length - Number of items inside your tuple
print(len(friends))

# Membership
print("Anshika" in friends)
print("Adib" in friends)

#Dictionary - Key-Value List = [] Tuple = () Dict = {}

Phonebook = {
    "Shomopriyo": 88579820832,
    "Tahseenul": 889347288374,
    "Anshika": 88299749820,
    "Subhadeep": 917029043892
}

# print(Phonebook)

# All Keys / Values
print(Phonebook.keys())
print(Phonebook.values())

#Access Elements
print(Phonebook.get("Shomopriyo"))
print(Phonebook.get("Anshika"))
print(Phonebook["Subhadeep"])

#Update
Phonebook["Anshika"] = 881111111
print(Phonebook.get("Anshika"))

#Remove
del Phonebook["Subhadeep"]
print(Phonebook)

#Add
Phonebook["Adib"]= 8800000000
print(Phonebook)

#loop
for names in Phonebook:
    print(names)

for key,value in Phonebook.items():
    print(key,value)