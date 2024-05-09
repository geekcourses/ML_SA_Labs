class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old. ")

class Blond():
    def think(self):
        print(f'{self.name} is thinking')


class Employee(Person, Blond):
    def __init__(self, name, age):
        super().__init__(name, age)
        # Person.__init__(self, name, age)

    def greet(self):
        super().greet()
        print('Says Employee....')

class Manager(Person):
    def __init__(self, name, age):
        super().__init__(name, age)



employee1 = Employee('John', 30)
manager1 = Manager('Jane', 40)

employee1.greet()
employee1.think()
manager1.greet()
