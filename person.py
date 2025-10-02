class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj = Person("Aleksandrs", 15)
#print(f"Sveiks, {obj.name}, tev ir {obj.age} gadi!")

class Animal:
    def __init__(self):
        pass

    def make_sound(self):
        print("Vau vau!")

dog = Animal()
dog.make_sound()    