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
name = "Diana"
number = len(name) * 3

print("Hello {}, your number is {}".format(name, number))
