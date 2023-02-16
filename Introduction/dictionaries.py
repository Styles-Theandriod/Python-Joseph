mbappe = {"firstname": "Kylian", "lastname": "Mbappe", "age": 23, "height": 1.78}

# print(mbappe.keys())
# print(mbappe.values())

# for key, value in mbappe.items():
#     sentence = "Mbappe's " + key + " is " + str(value)
#     print(sentence)  

# for key in mbappe.keys():
#     print(key.title())

# for value in mbappe.values():
#     print(value)

# for detail in mbappe.keys():
#     print(detail)


# ADDING VALUES TO A DICTIONARY
mbappe['club'] = "PSG"
mbappe['country'] = "France"

# print(mbappe)

# CHANGING VALUES IN A DICTIONARY
mbappe['club'] = "Real Madrid"
mbappe['country'] = "Nigeria"

# print(mbappe)

# STARTING WITH AN EMPTY DICTIONARY
maguire = {}

# print(maguire)

maguire['firstname'] = "Harry"
maguire['lastname'] = "Maguire"
maguire['age'] = 29
maguire['height'] = 1.89
maguire['club'] = "Man United"
maguire['country'] = "England"

# print(maguire)

# NESTING A DICTIONARIES IN A LIST
benzema = {"firstname": "Karim", "lastname": "Benzema"}
modric = {"firstname": "Luka", "lastname": "Modric"}
casemiro = {"firstname": "Henrique", "lastname": "Casemiro"}

madridBoys = [benzema, modric, casemiro]
print(madridBoys)

# NESTING A DICTIONARIES IN A DICTIONARIES
users = {
    "gabby": {
        "firstname": "Gabriel",
        "lastname": "De Suza",
        "profession": "Programmer"
    },
    "victory": {
        "firstname": "Victory",
        "lastname": "Churchill",
        "profession": "Programmer",
    },
    "blake": {
        "firstname": "Blake",
        "lastname": "Livingstone",
        "profession": "Sportsman",
    }
}

for key, value in users["gabby"].items():
    print("Gabby's", key, "is", value)

print(users)