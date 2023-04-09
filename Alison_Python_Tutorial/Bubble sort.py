list = [8,3,1,4] # declare a list
print(list)
 
 # original = 8314
 #3814
 #3184
 #3148
 #1348

lenght = len(list)# cast the list in a variable

for i in range (lenght): # for each value in the lenght, i also refers to the index so for the first iteration i=0
    for j in range (0, lenght-i-1): #leave out the raminig to indexes 
        if list[j] > list[j+1]: #condition for the first and second of the two indexes were dealing with
            list[j], list[j+1] = list[j+1] , list[j] #swap the items

print(list)
"""#How lenght function work
list = [8,3,1,4]

lenght = len(list)

print(lenght)"""


           