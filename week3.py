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


