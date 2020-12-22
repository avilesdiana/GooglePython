#Instance

"""
class Piglet:
    name = "piglet"
    def speak(self):
        print("Oik! I'm {}! Oink!".format(self.name))

hamlet = Piglet()
hamlet.name = "Hamlet"
print(hamlet.speak())

"""
"""
class Piglet:
    years = 0
    def pig_years(self):
        return self.years * 18


diana = Piglet()
diana.years = 15
print(diana.pig_years())

"""

#Constructor
"""
class Apple:
    def __init__(self,color, flavor):
        self.color = color
        self.flavor = flavor

diana = Apple("red", "sweet")
print(diana.color)
"""
"""
In this code, there's a Person class that has an attribute name, 
which gets set when constructing the object. Fill in the blanks so that 
1) when an instance of the class is created, the attribute gets set correctly, and 
2) when the greeting() method is called, the greeting states the assigned name."""

"""
class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is {}".format(self.name) 

# Create a new instance with a name of your choice
some_person = Person("diana")  
# Call the greeting method
print(some_person.greeting())

"""

"""
class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    
    def __str__(self):
        return "This apple is {} and it's flavor is {}". format(self.color, self. flavor)

diana = Apple("red", "Sweet")
print(diana)
"""
