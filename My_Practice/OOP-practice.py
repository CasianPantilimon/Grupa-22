"""
This is my own MyPracticeSessions documentation
"""


class PlayerCharacter:
    membership = True  # Class Object Attribute - not dynamic - all classes will get this attribute by default,

    # unlike .attack from line 16
    # de asemenea cred ca "membership ul" ar putea fi un input care ulterior sa fie evaluat la TRUE ptr a face
    # lucrurile mai dinamice
    def __init__(self, name, age, magic_power):
        if self.membership:
            self.name = name  # attributes
        self.age = age
        self.magic = magic_power

    def shout(self):
        return f"My name is {self.name}!!!!!"


player1 = PlayerCharacter("Cindy", 44, "ultra speed")
player2 = PlayerCharacter("Thomas", 22, "none")
player2.attack = 99

# print(player1.shout())
# print(player2.membership)

"""
A fun little exercise where you can find the oldest cat using MyPracticeSessions 
"""


# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat("Nero", 3)
cat2 = Cat("Felix", 2)
cat3 = Cat("Fury", 6)
# 2 Create a function that finds the oldest cat
my_cats_age = [cat3.age, cat2.age, cat1.age]


# print(my_cats_age)

def oldest_cat():
    for i in my_cats_age:
        return max(my_cats_age)


# print(oldest_cat())


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
# print(f"The oldest cat is {oldest_cat()} years old.")

class CaracterNou:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("run")

    def speak(self):
        return f"My name is {self.name} and I am {self.age} years old!"


jucator1 = CaracterNou("Casian", 26)
jucator2 = PlayerCharacter("Marcel", 44, "Immortality")
# print(jucator1.speak())
# print(jucator2.shout())

"""
- Mai jos putem vedea cum putem conecta mai multe MyPracticeSessions classes, importand dintr o clasa anumite proprietati.
"""


# intr un joc video avem mai multe caractere. magicieni, arcasi, etc.toti vor avea abilitatea de a ataca,
# dar specifica puterii lor, insa toti trebuie sa fie logati mai intai pentru a putea juca

class User:
    def signed_in(self):
        return "logged in"

    def email(self, email):
        self.email = email


class Magician(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        return f"My name is {self.name} and I am attacking with the power of {self.power}."


class Arcas(User):
    def __init__(self, name, arrows, email):
        self.name = name
        self.arrows = arrows
        self.email = email

    def attack(self):
        return f"My name is {self.name} and I am attacking with a number of:  {self.arrows} arrows."


magician1 = Magician("Gandalf", 55)
arcas1 = Arcas("Robin", 100, "robin@gmail.com")

print(arcas1.email)
# mai jos se poate observa ca ambii jucatori au abilitatea de a fi logati,
# deoarece mostenesc functia "signed in" de la clasa "USer" fara a mai fi necesar sa o rescriem
#
# print(magician1.signed_in())
# print(arcas1.signed_in())
# # mai jos se poate vedea ca abilitatea de "attack" este diferita pentru fiecare jucator
# print(magician1.attack())
# print(arcas1.attack())

# mai jos verificam daca un obiect este o instanta a unei clase
# print(isinstance(magician1, Arcas))
# print(isinstance(magician1, Magician))
# print(isinstance(magician1, User))
