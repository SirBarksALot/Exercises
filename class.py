class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.name, self.age)


class Dog(Animal):
    def barking(self, bark):
        self.barker = bark
        print(self.barker)


Shiro = Dog('Shiro', '5')
Shiro.barking('Auuuuuu!')


class Summing:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        output = self.x + other.x
        return output


num1 = Summing(4)
num2 = Summing(6)
print(num1 + num2)
