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
