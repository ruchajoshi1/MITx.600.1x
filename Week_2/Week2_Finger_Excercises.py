# week 2 Excercise 1
iteration = 0
count = 0
while iteration < 5:
    # the variable 'letter' in the loop stands for every 
    # character, including spaces and commas!
    for letter in "hello, world": 
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
#Iteration 0; count is: 12
#Iteration 1; count is: 24
#Iteration 2; count is: 36
#Iteration 3; count is: 48
#Iteration 4; count is: 60    

iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1     
#Iteration 0; count is: 12
#Iteration 1; count is: 12
#Iteration 2; count is: 12
#Iteration 3; count is: 12
#Iteration 4; count is: 12

iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
#Iteration 0; count is: 1
#Iteration 1; count is: 12
#Iteration 2; count is: 1
#Iteration 3; count is: 12
#Iteration 4; count is: 1    

# Excercise 2
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) >= epsilon:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))    
# infinite loop

x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))    
# succeeded: 4.999999999999998
    
# Excercise - guess my number
#The program works as follows: you (the user) thinks of an integer between 0 
#(inclusive) and 100 (not inclusive). The computer makes guesses, and you give 
#it input - is its guess too high or too low? Using bisection search, the 
#computer will guess the user's secret number!

low = 0
high = 100
print('Please think of a number between 0 and 100!')
while True:
    guess = (high + low)//2
    print('Is your secret number ' + str(guess) + ' ?')
    a = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if a == 'c':
        print('Game over. Your secret number was:', str(guess))
        break
    elif a == 'l':
        low = guess
    elif a == 'h':
        high = guess
    else:
        print('Sorry, I did not understand your input.')    
        
# Excercise Square
def square(x):
    '''
    x: int or float.
    '''
    # Your code here
    return x*x

# Excercise eval quadratic
def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    # Your code here
    return ((a*x*x) + (b*x) +c)        

# Excercise 3
def a(x, y, z):
     if x:
         return y
     else:
         return z

def b(q, r):
    return a(q>r, q, r)

a(False,2,3)
b(3,2)
a(3>2,a,b) 
b(a,b) 
        
# Excercise 4
a = 10
def f(x):
      return x + a
a = 3
f(1)
# int 4

x = 12
def g(x):
    x = x + 1
    def h(y):
        return x + y
    return h(6)
g(x)    
# int 19

#Excercise 5
def foo(x, y = 5):
   def bar(x):
      return x + 1
   return bar(y * 2)
          
foo(3)
# 11

def foo(x, y = 5):
   def bar(x):
      return x + 1
   return bar(y * 2)
          
foo(3, 0)
# 1

def foo (x):
   def bar (z, x = 0):
      return z + x
   return bar(3, x)

foo(2)
# 5

def foo (x):
   def bar (z, x = 0):
      return z + x
   return bar(3)

foo(5)
# 3

# Excercise 6
str1 = 'exterminate!' 
str2 = 'number one - the larch'    

str2 = str2.capitalize() 
str2
str2.swapcase()
str2.index('n')
str2.find('n')
str2.find('!')
str1 = str1.replace('e', '*') 
str1
str2.replace('one', 'seven')

# Exercise: fourth power
def fourthPower(x):
    '''
    x: int or float.
    '''
    # Your code here
    return square(square(x))

fourthPower(2)

# Exercise: odd
def odd(x):
    '''
    x: int

    returns: True if x is odd, False otherwise
    '''
    # Your code here
    return x%2 !=0

odd(4)

#Exercise: iter power
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    result = base
    if exp == 0:
        return 1
    else:
        for i in range(1, exp):
            result *= base
    return result

iterPower(5,3)

#Exercise: power recur
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)
    
recurPower(5,3)    

# Exercise: gcd iter
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    gcd = 1
    c = min(a, b)
    for i in range(c, 1, -1):
        if (a % i == 0) and (b % i == 0):
            gcd = i
            break
        else:
            gcd = 1
    return gcd

gcdIter(7,35)

# Exercise: gcd recur
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

gcdRecur(13,39)    

# Exercise: is in
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if aStr == "":
        return False
    elif len(aStr) == 1 and aStr == char:
        return True
    elif len(aStr) == 1 and aStr != char:
        return False
    elif aStr[len(aStr)//2] == char:
        return True
    else:
        if char < aStr[len(aStr)//2]:
            return isIn(char, aStr[:len(aStr)//2])
        else:
            return isIn(char, aStr[len(aStr)//2:])
        
isIn('r', 'adfaejarerjdfgjergh')      
     