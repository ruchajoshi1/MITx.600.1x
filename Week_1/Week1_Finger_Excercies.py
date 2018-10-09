
# Exercise: vara varb
#Assume that two variables, varA and varB, are assigned values, either numbers 
#or strings.

#Write a piece of Python code that evaluates varA and varB, and then prints 
#out one of the following messages:

#"string involved" if either varA or varB are strings

#"bigger" if varA is larger than varB

#"equal" if varA is equal to varB

#"smaller" if varA is smaller than varB

None
if type(varA) == str or type(varB) == str:
    print('string involved')
elif varA > varB:
    print('bigger')
elif varA == varB:
    print('equal')
elif varA < varB:
    print('smaller')
    
# Excercise 4
num = 0
while num <= 5:
    print(num)
    num += 1

print("Outside of loop")
print(num) 
# 0,1,2,3,4,5,Outside of loop,6

numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10:
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
print("Number of apples: " + str(numberOfApples))
# infinite loop

num = 10
while num > 3:
    num -= 1
    print(num)
# 9,8,7,6,5,4,3

num = 10
while True:
    if num < 7:
        print('Breaking out of loop')
        break
    print(num)
    num -= 1
print('Outside of loop')    
# 10,9,8,7,Breaking out of loop,Outside of loop

num = 100
while not False:
    if num < 0:
        break
print('num is: ' + str(num)) 
# infinite loop

# Excercise while loop
x = 2
while x < 11:
    print(x)
    x += 2
print('Goodbye!')
# 2 4 6 8 10 Goodbye!

y = 10
print('Hello!')
while y > 0:
    print(y)
    y -= 2
# Hello! 10 8 6 4 2     
    
total = 0
i = 0
end = 7
while i <= end:
    total += i
    i += 1

print(total)
# 28 (1+2+3+4+5+6+7)

# Excercise for loop
for i in range(2, 11, 2):
    print(i)
print('Goodbye!')
# 2 4 6 8 10 Goodbye!

print("Hello!")
for i in range(10, 1, -2):
    print(i)
# Hello! 10 8 6 4 2

total = 0
end = 5
for i in range(end+1):
    total += i
print(total)    
# 15 (1+2+3+4+5)
    
# Excercise 5
num = 10
for num in range(5):
    print(num)
print(num)
# 0 1 2 3 4 4

divisor = 2
for num in range(0, 10, 2):
    print(num/divisor) 
#  0.0,1.0,2.0,3.0,4.0   

for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print('Foo!') 
# 0,Foo!,4,8,12,16,Foo!       
        
for letter in 'hola':
    print(letter)          
# h,o,l,a    
    
count = 0
for letter in 'Snow!':
    print('Letter # ' + str(count) + ' is ' + str(letter))
    count += 1
    break
print(count)
# Letter # 0 is S,1   

# Excercise 6
myStr = '6.00x'

for char in myStr:
    print(char)

print('done')
# 6,.,0,0,x,done

greeting = 'Hello!'
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print(letter)
    print(letter)

print('done')
# H,e,e,l,l,l,o,!,!,done

school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1

print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons)) 
# M, numVowels is : 11, numCons is :-25

# Excercise 7
iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
#Iteration 0; count is: 12
#Iteration 1; count is: 24
#Iteration 2; count is: 36
#Iteration 3; count is: 48
#Iteration 4; count is: 60
    
for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count)) 
# infinite loop

for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))
        break        
#Iteration 0; count is: 12
#Iteration 1; count is: 12
#Iteration 2; count is: 12
#Iteration 3; count is: 12
#Iteration 4; count is: 12    
        
count = 0
phrase = "hello, world"
for iteration in range(5):
    index = 0
    while index < len(phrase):
        count += 1
        index += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))    
#Iteration 0; count is: 12
#Iteration 1; count is: 24
#Iteration 2; count is: 36
#Iteration 3; count is: 48
#Iteration 4; count is: 60    
    
count = 0
phrase = "hello, world"
for iteration in range(5):
    while True:
        count += len(phrase)
        break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
#Iteration 0; count is: 12
#Iteration 1; count is: 24
#Iteration 2; count is: 36
#Iteration 3; count is: 48
#Iteration 4; count is: 60
    
count = 0
phrase = "hello, world"
for iteration in range(5):
    count += len(phrase)
    print("Iteration " + str(iteration) + "; count is: " + str(count)) 
#Iteration 0; count is: 12
#Iteration 1; count is: 24
#Iteration 2; count is: 36
#Iteration 3; count is: 48
#Iteration 4; count is: 60
