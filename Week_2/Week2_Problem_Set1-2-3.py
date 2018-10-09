# Problem 1 - Paying Debt off in a Year
#Write a program to calculate the credit card balance after one year if a 
#person only pays the minimum monthly payment required by the credit card 
#company each month.

#The following variables contain values as described below:

#balance - the outstanding balance on the credit card

#annualInterestRate - annual interest rate as a decimal

#monthlyPaymentRate - minimum monthly payment rate as a decimal

#For each month, calculate statements on the monthly payment and remaining 
#balance. At the end of 12 months, print out the remaining balance. Be sure to 
#print out no more than two decimal digits of accuracy - so print

#A summary of the required math is found below:

#Monthly interest rate= (Annual interest rate) / 12.0
#Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
#Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
#Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate
#                             x Monthly unpaid balance)

for i in range(12):
    balance = balance - (balance * monthlyPaymentRate) + ((balance - (balance 
                        * monthlyPaymentRate)) * (annualInterestRate/12))
print("Remaining balance:", round(balance, 2))

# Problem 2
#Now write a program that calculates the minimum fixed monthly payment needed in
#order pay off a credit card balance within 12 months. By a fixed monthly 
#payment, we mean a single number which does not change each month, but instead 
#is a constant amount that will be paid each month.

#In this problem, we will not be dealing with a minimum monthly payment rate.

#The following variables contain values as described below:

#balance - the outstanding balance on the credit card

#annualInterestRate - annual interest rate as a decimal

#The program should print out one line: the lowest monthly payment that will pay
#off all debt in under 1 year.

# Paste your code into this box
monthlyPaymentRate = 0
init_balance = balance
monthlyInterestRate = annualInterestRate/12

while balance > 0:
    for i in range(12):
        balance = balance - monthlyPaymentRate + ((balance - monthlyPaymentRate)
        * monthlyInterestRate)
    if balance > 0:
        monthlyPaymentRate += 10
        balance = init_balance
    elif balance <= 0:
        break
print('Lowest Payment:', monthlyPaymentRate)

# Problem 3
#Monthly interest rate = (Annual interest rate) / 12.0
#Monthly payment lower bound = Balance / 12
#Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

#Write a program that uses these bounds and bisection search (for more info 
#check out the Wikipedia page on bisection search) to find the smallest monthly 
#payment to the cent (no more multiples of $10) such that we can pay off the 
#debt within a year. Try it out with large inputs, and notice how fast it is 
#(try the same large inputs in your solution to Problem 2 to compare!). Produce 
#the same return value as you did in Problem 2.

# Paste your code into this box
init_balance = balance
monthlyInterestRate = annualInterestRate/12
lower = init_balance/12
upper = (init_balance * (1 + monthlyInterestRate)**12)/12.0
epsilon = 0.03

while abs(balance) > epsilon:
    monthlyPaymentRate = (upper + lower)/2
    balance = init_balance
    for i in range(12):
        balance = balance - monthlyPaymentRate + ((balance - monthlyPaymentRate) * monthlyInterestRate)
    if balance > epsilon:
        lower = monthlyPaymentRate
    elif balance < -epsilon:
        upper = monthlyPaymentRate
    else:
        break
print('Lowest Payment:', round(monthlyPaymentRate, 2))

