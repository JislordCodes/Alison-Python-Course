"""#Tuples: A list that cannot be edited, you dont want any modification its mutable
tuple1 = (12, 13, 11, 13)
tuple[1] = 16 #your tuple cant be reassigned"""

#convert list to a tuple
list = [1,2,3,4]
tuple1 = tuple(list)
print(tuple1)

#convert tuple to list then modify then return it back to a tuple
tup1 = (1,2,3,4,5)
l1 = list(tup1)
l1[3] = 4
tup1 = tuple(l1)
print(tup1)