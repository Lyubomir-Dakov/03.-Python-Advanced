from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def animal_sound(self):
        pass


class Cat(Animal):
    def animal_sound(self):
        return 'meow'


class Dog(Animal):
    def animal_sound(self):
        return 'woof-woof'


class Chicken(Animal):
    def animal_sound(self):
        return 'peow-peow'


def animal_sound(animals: list):
    for animal in animals:
        print(animal.animal_sound())


animals = [Cat(), Dog(), Chicken()]
animal_sound(animals)
