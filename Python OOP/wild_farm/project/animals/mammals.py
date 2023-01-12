from project.animals.animal import Mammal
from project.food import Food


class Mouse(Mammal):
    eaten_food = 0

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, food: Food):
        if food.__class__.__name__ == 'Vegetable' or food.__class__.__name__ == 'Fruit':
            self.weight += food.quantity * 0.1
            Mouse.eaten_food += food.quantity
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {Mouse.eaten_food}]"


class Dog(Mammal):
    eaten_food = 0

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def feed(self, food: Food):
        if food.__class__.__name__ == 'Meat':
            self.weight += food.quantity * 0.4
            Dog.eaten_food += food.quantity
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {Dog.eaten_food}]"


class Cat(Mammal):
    eaten_food = 0

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def feed(self, food: Food):
        if food.__class__.__name__ == 'Vegetable' or food.__class__.__name__ == 'Meat':
            self.weight += food.quantity * 0.3
            Cat.eaten_food += food.quantity
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {Cat.eaten_food}]"


class Tiger(Mammal):
    eaten_food = 0

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food: Food):
        if food.__class__.__name__ == 'Meat':
            self.weight += food.quantity
            Tiger.eaten_food += food.quantity
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {Tiger.eaten_food}]"
