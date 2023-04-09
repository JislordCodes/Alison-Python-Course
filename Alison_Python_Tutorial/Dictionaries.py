"""A dictionary is decalred by '{}' and inside it is a key and each key as assiosiated value e.g {
"name" : "John"
"age" : 39
}
"""

employee = {
    'name' : 'John Smith',
    'age' : 39,
    'Salary' : '$10,000',
    'Designation' : 'Manager'
}

print(employee['name'], employee['age'])

#Print out the keys with the featues there assigned to
for key in employee:
    print(key + ":" + str(employee[key]))#str(employee[key]) print out the key features
