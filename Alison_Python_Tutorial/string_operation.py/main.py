"""write a code that returns the letters and numerics of 'ABC123DEF456'"""

a = 'ABC123DEF456CAC3333ZNABUEB3B3BBU33U3U3B32223'


print("**************")

list = list(a)

def function(list):
    for i in range(0, len(list)):  
        letters = [ ]
        numerics = [ ]     
        for j in list:
            if j.isdigit() == True:
                numerics.append(j)
            else:
                letters.append(j)
    
    
    numerics_int = [int(x) for x in numerics]
    print(letters)
    print(numerics_int)  
    print("sum of the numbers: ",sum(numerics_int))
function(list)