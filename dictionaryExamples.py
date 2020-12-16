"""
file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
print(file_counts)
print(file_counts["txt"])

print("jpg" in file_counts)
print("html" in file_counts)

#Add other value
file_counts["cfg"] = 8
print(file_counts)

#Change the value
file_counts["jpg"] = 11
print(file_counts)

#Remove value
del file_counts["py"]
print(file_counts)
"""
"""
Print:
{'jpg': 10, 'txt': 14, 'csv': 2, 'py': 23}
14
True
False
{'jpg': 10, 'txt': 14, 'csv': 2, 'py': 23, 'cfg': 8}
{'jpg': 11, 'txt': 14, 'csv': 2, 'py': 23, 'cfg': 8}
{'jpg': 11, 'txt': 14, 'csv': 2, 'cfg': 8}
"""

#Example Video
"""
The "toc" dictionary represents the table of contents for a book. 
Fill in the blanks to do the following: 
1) Add an entry for Epilogue on page 39. 
2) Change the page number for Chapter 3 to 24. 
3) Display the new dictionary contents. 
4) Display True if there is Chapter 5, False if there isn't.
"""

"""
toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc ["Epilogue"] = 39 # Epilogue starts on page 39
toc ["Chapter 3"] = 24# Chapter 3 now starts on page 24
print(toc) # What are the current contents of the dictionary?
print("Chapter 5" in toc) # Is there a Chapter 5?
"""


"""
print:

{'Introduction': 1, 'Chapter 1': 4, 'Chapter 2': 11, 'Chapter 3': 24, 'Chapter 4': 30, 'Epilogue': 39}
False
"""

"""
#Itering over the Contents of a dictionary

file_counts = {"jpg": 10, "txt":14, "csv":2, "py":23}

for extension in file_counts:
    print(extension)

#Other form

for ext, amount in file_counts.items():
    print("There are {} files with the .{} extension".format(amount,ext))

#Other form for print
print(file_counts.keys())
print(file_counts.values())

for value in file_counts.values():
    print(value)

"""

#Example
"""
Remember that the items method returns a tuple of key, value for each element in the dictionary. 
"""
"""
cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for key,value in cool_beasts.items():
    print("{} have {}".format(key,value))
"""


""""
#Other form
def count_letters(text):
    result = {}

    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

print(count_letters("aaaaaa"))
print(count_letters("diana Aviles"))
print(count_letters("a long string with a lot of letter"))
"""

#DICTIONARIES VS. LISTS

"""
To workaround this, our single value can be a list containing multiple values. 
Here we have a dictionary called "wardrobe" with items of clothing and their colors. 
Fill in the blanks to print a line for each item of clothing with each color, 
for example: "red shirt", "blue shirt", and so on.
"""
"""
wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for item, color in wardrobe.items():
	for colorsub in color:
		print("{} {}".format(colorsub,item))
"""


"""
red shirt
blue shirt
white shirt
blue jeans
black jeans
"""