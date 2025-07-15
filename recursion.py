# FACTORIAL OF A NUMBER USING ITERATION.
def factorial(n):
    result = 1  # Initialize result to 1
    for i in range(1, n + 1):  # Loop through numbers 1 to n
        result *= i  # Multiply result by i at each iteration
    return result  # Return the final factorial
n = 5
print(f"The factorial of {n} is {factorial(n)}")

#FACTORIAL OF A NUMBER USING RECURSION
def factorial(n):
    if n==0 or n==1:
        return 1 #base case of their factorials
    else:
        return n*factorial(n-1)#recursive call
n=6
print(f"The factorial of {n} is {factorial(n)}")

#POWER OF A NUMBER USING ITERATION
def power(base,exponent):
    result=1
    for i in range(1,exponent+1):
        result*=base
    return result
base=2
exponent=5
print(f"{base} to the power of {exponent} is {power(base,exponent)}")

#POWER OF A NUMBER USING RECURSION
def power(base, exponent):
    if(exponent==1):
        return base
    else:
        return base*power(base,exponent-1)
base=5
exponent=3
print(f"{base} to the power of {exponent} is {power(base,exponent)}")

#FIBONNACCI SERIES USING ITERATION
#Using a For Loop
def fibonacci(n):
    a, b = 0, 1
    print("For loop:", end=" ")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

#Using a While Loop
def fibonacci_while_loop(n):
    a, b = 0, 1
    count = 0
    print("While loop:", end=" ")
    while count < n:
        print(a, end=" ")
        a, b = b, a + b
        count += 1
    print()

#RECURSION USING RECURSIVE
# Python program to display the Fibonacci sequence
def recursive(n):
   if n <= 1:
       return n
   else:
       return(recursive(n-1) + recursive(n-2))
n = 10
# check if the number of terms are valid
if n <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(n):
       print(recursive(i))



