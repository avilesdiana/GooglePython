#Week 4
# by Diana Aviles

#Modify the first_and_last function so that it returns 
#True if the first letter of the string is the same as the last letter 
# of the string, False if they’re different. 

"""
def first_and_last(message):
    if not message or message[0] == message[-1]:
        return True
    else:
        return False
    

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))
"""

"""
def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email [:index] + "@" + new_domain
        return new_email
    return email

print(replace_domain("laura150429@hotmail.com", "hotmail.com", "outlook.com"))
"""

#Fill in the gaps in the initials function so that it returns the initials of the words 
# containeefed in the phrase received, in upper case. 
# For example: "Universal Serial Bus" should return "USB"; "local area network" should return "LAN”. 
"""
def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0].upper()
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN

"""
#Examples with format
"""
name = "Diana"
number = len(name) * 3

print("Hello {}, your number is {}".format(name, number))
"""
#Formatting expression
"""
price = 7.5
with_tax = price * 1.09
print(price, with_tax)
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price,with_tax))
"""

#other example
"""
def to_celsius(x):
    return(x-32)*5/9

for x in range(0,101,10):
    print("{:>3} F | {:>6.2f} C".format(x,to_celsius(x)))

"""
"""
 RESULT: 
  0 F | -17.78 C
 10 F | -12.22 C
 20 F |  -6.67 C
 30 F |  -1.11 C
 40 F |   4.44 C
 50 F |  10.00 C
 60 F |  15.56 C
 70 F |  21.11 C
 80 F |  26.67 C
 90 F |  32.22 C
100 F |  37.78 C
"""

#Using the format() method
# "base string with {} placeholders".format(variables)
"""
example = "format() method"

formatted_string = "this is an example of using the {} on a string".format(example)

print(formatted_string)
"""
"""Outputs:
this is an example of using the format() method on a string
"""

#If the placeholders indicate a number, they’re replaced by the variable 
# corresponding to that order (starting at zero).

# "{0} {1}".format(first, second)

"""
first = "apple"
second = "banana"
third = "carrot"

formatted_string = "{0} {2} {1}".format(first, second, third)

print(formatted_string)
"""
"""Outputs:
apple carrot banana
"""
#The important difference 
# with the format method is that it takes
#  the value of the variables from the 
# current context, instead of taking the values from parameters.
"""
name = "Diana"
print(f'Hello {name}')

"""
"""
item = "Purple Cup"
amount = 5
price = amount * 3.25

print(f'item:{item} - Amount: {amount} - Price:{price:.2f}')

"""
