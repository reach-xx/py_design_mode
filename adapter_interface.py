import os


class Dog(object):
    def __init__(self):
        print('----------init-----------dog')
        self.name = "Dog"

    def bark(self):
        print('woof-------bark-------------')
        return "woof!"


class Cat(object):
    def __init__(self):
        print('-----------init----------cat')
        self.name = "Cat"

    def meow(self):
        print('-----------meow---------cat')
        return "meow!"


class Human(object):
    def __init__(self):
        print('-----------human---------init')
        self.name = "Human"

    def speak(self):
        print('--------------speak---------human')
        return "'hello'"


class Car(object):
    def __init__(self):
        print('-----------------init--------car')
        self.name = "Car"

    def make_noise(self, octane_level):
        print('noise----------------------car')
        return "vroom%s" % ("!" * octane_level)


class Adapter(object):
    """
    Adapts an object by replacing methods.
    Usage:
    dog = Dog
    dog = Adapter(dog, dict(make_noise=dog.bark))
    """
    def __init__(self, obj, adapted_methods):
        print('adapter--------------------init')
        """We set the adapted methods in the object's dict"""
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        print('getattr------------------:',attr)
        """All non-adapted calls are passed to the object"""
        return getattr(self.obj, attr)


def main():
    objects = []
    print('-----------------------1')
    dog = Dog()
    print('-----------------------2')
    objects.append(Adapter(dog, dict(make_noise=dog.bark)))
    print('-----------------------3')
    cat = Cat()
    print('-----------------------4')
    objects.append(Adapter(cat, dict(make_noise=cat.meow)))
    print('-----------------------5')
    human = Human()
    objects.append(Adapter(human, dict(make_noise=human.speak)))
    car = Car()
    car_noise = lambda: car.make_noise(3)
    objects.append(Adapter(car, dict(make_noise=car_noise)))

    for obj in objects:
        print("A", obj.name, "goes", obj.make_noise())


if __name__ == "__main__":
    main()

