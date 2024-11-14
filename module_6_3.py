# Ошибка эволюции

from random import randint

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        if dz < 0:
            print('Здесь слишом глубоко, я не могу нырнуть :(')
        else:
            self._cords = [dx * self.speed, dy * self.speed, dz * self.speed]

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER <= 5:
            print('Извините, я настроен миролюбиво :)')
        elif self._DEGREE_OF_DANGER > 5:
            print('Будь осторожен, я атакую тебя 0_0')

    def speak(self):
        if self.sound:
            print(self.sound)


class Brid(Animal):
    beak = True

    def lay_eggs(self):
        print(f'Вот (есть) {randint(1, 4)} яиц для тебя')


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        x = self._cords[0]
        y = self._cords[1]
        z = int(self._cords[2] - abs(dz) / 2 * self.speed)
        # self.move(x, y, z)
        self._cords[2] = int(self._cords[2] - abs(dz) / 2 * self.speed)
        print(x, y, z)


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(Brid, PoisonousAnimal, AquaticAnimal):
    sound = "Click-click-click"


if __name__ == '__main__':

    db = Duckbill(10)

    print(db.live)
    print(db.beak)

    db.speak()
    db.attack()

    db.move(1, 2, 3)
    db.get_cords()
    db.dive_in(6)
    db.get_cords()

    db.lay_eggs()