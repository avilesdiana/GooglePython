"""x = ["Now", "we", "are", "Cooking"]
print(type(x))
print(x)

print(len(x))

print("are" in x)

"""

"""
Using the "split" string method from the preceding lesson, complete the get_word function to return 
the {n}th word from a passed sentence. For example, get_word("This is a lesson about lists", 
4) should return "lesson", which is the 4th word in this sentence. Hint: remember that list 
indexes start at 0, not 1. 

"""
"""
def get_word(sentence, n):
	# Only proceed if n is positive 
	if n > 0:
		words = sentence.split()
		# Only proceed if n is not more than the number of words 
		if n <= len(words):
			return(words[n-1])
	return("")

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing

"""
"""
fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.append("kiwi")
print(fruits)

fruits.insert(0,"Orange")
print(fruits)

fruits.remove("Melon")
print(fruits)

fruits.pop(3)
print(fruits)

fruits[2] = "pear"
print(fruits)

"""

"""
The skip_elements function returns a list containing every other element 
from an input list, starting with the first element. Complete this function to do that, 
using the for loop to iterate through the input list.
"""


"""
Let's use tuples to store information about a file: its name, its type and its size in bytes. 
Fill in the gaps in this code to return the size in kilobytes (a kilobyte is 1024 bytes) up to 2 decimal places. 
"""

"""
def file_size(file_info):
	name, type, size= file_info
	return("{:.2f}".format(size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21

"""
"""
The skip_elements function returns a list containing every other element from an input list, 
starting with the first element. Complete this function to do that, using the for loop to
 iterate through the input list.
"""
"""
def skip_elements(elements):
	# Initialize variables
	new_list = []
	i = 0

	# Iterate through the list
	for i in range(len(elements)):
		# Does this element belong in the resulting list?
		if i%2==0:
			# Add this element to the resulting list
			new_list.append(elements[i])
		# Increment i
		

	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []
"""

#Example iterating over list and Tuples

#List
"""
animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0

for animal in animals:
	chars += len(animal)

print("Total Characters: {}, Average lenght: {}".format(chars, chars/len(animals)))
"""
#Enumerate
"""
winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
	 print("{} - {}".format(index + 1, person))
"""

#Enumerate example
"""
Complete the skip_elements function to return every other element from the list, 
this time using the enumerate function to check if an element is on an even position or an odd position.
"""

"""
def skip_elements(elements):
	# code goes here
	new_list= []
	for index,word in enumerate(elements):
		if index%2 ==0:
			new_list.append(word)
	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
"""

#Other example

def full_emails(people):
	result = []
	for email, name in people:
		result.append("{} <{}>".format(name,email))
	return result


print(full_emails([("diana@example.com", "Diana Aviles"),("Bernardo@example.com", "Bernardo MG")]))