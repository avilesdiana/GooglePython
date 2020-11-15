#Week 4
# by Diana Aviles

#Modify the first_and_last function so that it returns 
#True if the first letter of the string is the same as the last letter 
# of the string, False if they’re different. 

def first_and_last(message):
    if not message or message[0] == message[-1]:
        return True
    else:
        return False
    

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))