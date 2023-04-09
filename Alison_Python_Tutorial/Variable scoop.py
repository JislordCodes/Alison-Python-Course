x = 10 #exists in a global scope
def function():
    x = 20 #exits in a local scope, so it dosent call the variable within the function 
function()
print(x)

"""x = 10 #exists in a global scope
def function():
    global x #turn it to a global variable
    x = 20
function()
print(x)"""