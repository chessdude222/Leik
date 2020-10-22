# Oppgave a
class Person:
    def __init__(self, name, age, gender): # Define the given arguments for the constructor
        self.name = name
        self.age = age
        self.gender = gender
#Oppgave b
    def change_name(self, name):        # Function that takes input name, and changes the name
        self.name = name
    def change_age(self, age):          # Function that takes input age, and changes the age
        self.age = age
    def change_gender(self, gender):    # Function that takes input gender, and changes the gender
        self.gender = gender

    def __str__(self):
        return f'name is {self.name}, age is {self.age}, gender is {self.gender}'
# Oppgave c
john = Person('John', 55, 'Male')       # Creates an instance of the class
print(john)                             # Prints out the instance
john.change_name('Sandra')              # Changes the name
john.change_gender('Female')            # Changes the gender
print(john)                             # Prints out the updated instance

"""
Terminal > python class_people.py
name is John, age is 55, gender is Male
name is Sandra, age is 55, gender is Female
"""
