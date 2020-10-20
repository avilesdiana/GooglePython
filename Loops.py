#WEEK 3
#Exercise by Diana Aviles

print("\n Introduction to loops\n")

#Anatomy of a While Loop
"""
x=0
while x < 5:
    print("Not there yet, x=" + str(x))
    x = x + 1
print("x =  " + str(x))
"""
# More while loop Examples
"""
def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
    
attempts(7)
"""
#Why initializaing variables matters
"""my_variable= 5
while my_variable < 10:
    print("Hello")
    my_variable +=1
"""
#Whenever you're writing a loop, check that you're initializing all the variables you want to use before you use them 
"""
def count_down(start_number):
  while (start_number > 0):
    print(start_number)
    start_number -= 1
  print("Zero!")


count_down(3)
"""
#Infinite Loops
"""def print_range(start, end):
	# Loop through the numbers from start to end
	n = start
	while n <= end:
		print(n)
		n+=1

print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 
"""
#Quiz
"""def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor +=1
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT
"""
#QUIZ 2
"""
def is_power_of_two(n):
  # Check if the number can be divided by two without a remainder
  while (n % 2 == 0 and n>0):
    n = n / 2
  # If after dividing by two the number is 1, it's a power of two
  if n == 1:
    return True
  return False
  

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False
"""

#Fill in the empty function so that it returns the sum of all the divisors of a number, 
# without including it. A divisor is a number that divides into another without a remainder.

"""def sum_divisors(n):
  sum = 0
  # Return the sum of all divisors of n, not including n
  x = 1

  while x < n:
    if n % x == 0:
      sum+=x
      x+=1
    else:
      x+=1
      
  return sum


print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114

# The multiplication_table function prints the results of a number 
# passed to it multiplied by 1 through 5. An additional requirement is
#  that the result is not to exceed 25, which is done with the break statement. 
# Fill in the blanks to complete the function to satisfy these conditions.
def multiplication_table(number):
	# Initialize the starting point of the multiplication table
	multiplier = 1
	# Only want to loop through 5
	while multiplier <= 5:
		result = multiplier * number 
		# What is the additional condition to exit out of the loop?
		if result > 25 :
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		# Increment the variable for the loop
		multiplier += 1

multiplication_table(3) 
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5) 
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)	
# Should print: 8x1=8 8x2=16 8x3=24

"""

#For Loops
"""
sum_squares function, so that it returns the sum of all the squares of 
numbers between 0 and x (not included). Remember that you can use the range(x) 
function to generate a sequence of numbers from 0 to x (not included).

def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum

print(sum_squares(10)) # Should be 285
"""
"""
values = [23,52,59,37,48]
sum = 0
length = 0

for value in values:
    sum += value
    length+=1

print("Total sum: " + str(sum)+ " - Average: " + str(sum/length))
"""

"""
In math, the factorial of a number is defined as the product of an integer 
and all the integers below it. For example, the factorial of four (4!) 
is equal to 1*2*3*4=24. Fill in the blanks to make the factorial function 
return the right number.


def factorial(n):
    result = 1
    for i in range(1,n):
        result += result * i
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120

"""
#Convert to celsius
"""
To quickly recap the range() function when passing one, two, or three parameters:

    One parameter will create a sequence, one-by-one, from zero to one less than the parameter.
    Two parameters will create a sequence, one-by-one, from the first parameter to one less than the second parameter.
    Three parameters will create a sequence starting with the first parameter and stopping before the second parameter, 
         but this time increasing each step by the third parameter.
"""
"""
def to_celsius(x):
    return (x-32)*5/9

for x in range(0,101,10):
    print(x,to_celsius(x))
"""

#Nested for loops

"""
for left in range(7):
    for right in range(left,7):
        print("[" + str(left)+ " ¨ " + str(right) + "]", end =" ")
    print()
"""
"""
teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
       if home_team != away_team:
           print(home_team + " vs " + away_team)

"""
#Quiz
"""
Fill in the blanks to make the factorial function return the factorial of n. 
Then, print the first 10 factorials (from 0 to 9) with the corresponding number. 
Remember that the factorial of a number is defined as the product of an integer 
and all integers before it. For example, the factorial of five (5!) 
is equal to 1*2*3*4*5=120. Also recall that the factorial of zero (0!) is equal to 1.
"""
"""
def factorial(n):
    result = 1
    for x in range(1,n):
        result = result * x
    return result

for n in range(0,10):
    print(n, factorial(n+1))

"""
#Factorial with Recursion
"""
recursion structure
def recursive_function(parameters):
    if base_case_condition(parameters):
        return base_case_value
    recursive_function(modified_parameters)
"""
"""
def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return 0

    # The recursive case is adding this number to 
    # the sum of the numbers smaller than this one.
    return  n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15
"""

#Quiz Recursion
"""
Fill in the blanks to make the is_power_of function return whether the number is a
 power of the given base. Note: base is assumed to be a positive number. Tip: 
 for functions that return a boolean value, you can return the result of a comparison. """

"""
def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number ==1:
    return True
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return False
  number /= base

  # Recursive case: keep dividing number by base.
  return is_power_of(number, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False

"""
"""
The count_users function recursively counts the amount of users that belong to a group 
in the company system, by going through each of the members of a group and if one of them 
is a group, recursively calling the function and counting the members. But it has a bug! 
Can you spot the problem and fix it?
"""

"""
def count_users(group):
  count = 0
  for member in get_members(group):
    count += 1
    if is_group(member):
      count -=1
      count += count_users(member)
  return count

print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18
"""

"""
Implement the sum_positive_numbers function, as a recursive function that returns the 
sum of all positive numbers between the number n received and 1. For example, when n 
is 3 it should return 1+2+3=6, and when n is 5 it should return 1+2+3+4+5=15.
"""
"""
def sum_positive_numbers(n):
   
  if n < 1: 
    return n
  return n+ sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15
"""

"""
Complete the function digits(n) that returns how many digits the number has. 
For example: 25 has 2 digits and 144 has 3 digits. Tip: you can figure out the digits of
 a number by dividing it by 10 once per digit until there are no digits left. """

"""
def digits(n):
	count = 0
	if n == 0:
	  count = 1
	while (n != 0 ):
		count += 1
		n//=10
	return count
	
print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1
print(digits(123456789)) #Should print 9
"""
"""
This function prints out a multiplication table (where each number is the 
result of multiplying the first number of its row by the number at the top
 of its column). Fill in the blanks so that calling multiplication_table(1, 3) 
 will print out:

1 2 3

2 4 6

3 6 9

"""
"""
def multiplication_table(start, stop):
	for x in range(start,stop+1):
		for y in range(start,stop +1):
			print(str(x*y), end=" ")
		print()

multiplication_table(1, 3)
# Should print the multiplication table shown above
"""


"""Pregunta 5

The counter function counts down from start to stop when start is bigger than stop, 
and counts up from start to stop otherwise. Fill in the blanks to make this work correctly. """

"""
def counter(start, stop):
	x = start
	if x > stop:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			if x > stop:
				return_string += ","
			x= x-1
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if x< stop:
				return_string += ","
			x = x+1
	return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"

"""

"""
The even_numbers function returns a space-separated string of all positive numbers that are 
divisible by 2, up to and including the maximum that's passed into the function. For example, 
even_numbers(6) returns “2 4 6”. Fill in the blank to make this work. """

"""
def even_numbers(maximum):
	return_string = ""
	for x in range(2,maximum+1):
		if(x%2 ==0):
			return_string += str(x) + " "
	return return_string.strip()

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed
"""
