"""def reverse(string):
    print(string[::-1])

reverse("hello")"""


"""def reverse(string):
    print(string[::-1])

    #Put it in a variable
reversedString = reverse('hello')

print('data', reversedString)#This is to show that the reversed string variable is empty
"""

#Get data to return through your function
def reverse(string):
    return string[::-1]

    #Put it in a variable
reversedString = reverse('hello')

print('data', reversedString) # we can see that the reversed string variable is assigned to reverse('hello') because we used return.