
'''Factory Method'''

class Dog:
    def __init__(self):
        self.eat = 'Dog Food'
        self.name= 'Dog'

    def get_name(self):
        return self.name

    def get_eat(self):
        return self.eat

class Cat:
    def __init__(self):
        self.eat = 'Cat Food'
        self.name = 'Cat'

    def get_name(self):
        return self.name

    def get_eat(self):
        return self.eat

def get_animal_func(name):
    func = dict(dog = Dog, cat = Cat)
    return func[name]()


d, c = get_animal_func('dog'), get_animal_func('cat')


print(d.get_name())
print(c.get_name())




