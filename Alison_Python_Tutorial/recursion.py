#factorial with python

#Recusion is when a function is called again and again to do something
def iterativeFactorial(n):
    result = 1
    for i in range(n,0,-1): #-1 is there because we set it to reverse order 5*4*3*2*1
        result = result * i
        print(result)
    return result

print(iterativeFactorial(5))

print("******************")
#Recursively
def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))