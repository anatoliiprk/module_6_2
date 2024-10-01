print('------\nЗадача "Изменять нельзя получать"\n------')

class Vehicle:

    __COLOR_VARIANTS = ['black', 'white', 'gray', 'yellow', 'brown']

    def __init__(self, owner: str, __model: str, __engine_power: int, __color: str):
        self.owner = owner
        self.__model = __model
        self.__endine_power = __engine_power
        self.__color = __color

    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_horsepower (self):
        print(f'Мощность двигателя: {self.__endine_power}')

    def get_color (self):
        print(f'Цвет: {self.__color}')

    def print_info (self):
        print('')
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: {self.owner}\n')

    def set_color (self, new_color: str):
        _new_color = new_color.lower()
        if _new_color in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGER_LIMIT = 5

vehicle1 = Sedan('Ivan', 'LADA 2110', 72, 'gray')

vehicle1.print_info()

vehicle1.set_color('Blue')
vehicle1.set_color('Brown')
vehicle1.owner = 'Stepan'

vehicle1.print_info()

print('------')