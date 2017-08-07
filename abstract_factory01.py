import random


class apple:
    def __str__(self):
        return 'Apple'

    def taste(self):
        return 'sweet'


class Strawberry:
    def __str__(self):
        return 'Berry'

    def taste(self):
        return 'sour'


class fruitShop:
    def __init__(self, fruit_type= None):
        self.fruit = fruit_type

    def showFruit(self):
        ft = self.fruit()
        if not ft is None:
            print('fruit name:', str(ft))
            print('fruit taste :', ft.taste())


def get_fruit():
    return random.choice([apple, Strawberry])

if __name__ == '__main__':
    fs = fruitShop()
    for i in range(5):
        fs.fruit = get_fruit()
        print('='*20)
        fs.showFruit()
        print('='*40)




