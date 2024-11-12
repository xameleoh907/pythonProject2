# Съедобное, несъедобное

class Animal:
    alive = True # живой
    fed = False # накормленный

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        self.food = Plant
        if food.edible:
            print(f'{self.name} съел {food.name}')
            Animal.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            Animal.alive = False


class Plant: # растение
    edible = False # съедобность

    def __init__(self, name):
        self.name = name


class Mammal(Animal): # млекопитающее
    # def eat наследуется из родительского класса
    pass


class Predator(Animal): # хищник
    # def eat наследуется из родительского класса
    pass


class Flower(Plant): # цветок
    pass


class Fruit(Plant): # фрукт
    edible = True


if __name__ == '__main__':

    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')
    #
    print(a1.name)
    print(p1.name)
    # #
    print(a1.alive)
    print(a2.fed)
    a1.eat(p1)
    a2.eat(p2)
    print(a1.alive)
    print(a2.fed)