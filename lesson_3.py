from enum import Enum


class Color(Enum):
    BLUE = '\33[34m'
    GREEN = '\33[32m'
    SILVER = '\33[90m'
    RED = '\33[31m'


# Mixin
class MusicPlayable:

    def play_music(self, song):
        print(f'Now is playing {song}')

    def stop_music(self):
        print('Music stopped')


class Drawable:
    def draw(self, emoji):
        print(emoji)


class SmartPhone(MusicPlayable, Drawable):
    pass


class Car(MusicPlayable, Drawable):
    def __init__(self, model, year, color):
        self.__model = model
        self.__year = year
        if isinstance(color, Color):
            self.__color = color

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    def drive(self):
        print(f'Car {self.__model} is driving')

    def __str__(self):
        return f'Model {self.__model} Year: {self.__year} Color: {self.__color.value}{self.__color.name}' + '\033[0m'

    def __gt__(self, other):
        return self.__year > other.__year

    def __lt__(self, other):
        return self.__year < other.__year

    def __le__(self, other):
        return self.__year <= other.__year

    def __ge__(self, other):
        return self.__year >= other.__year

    def __eq__(self, other):
        return self.__year == other.__year

    def __ne__(self, other):
        return self.__year != other.__year


class ElectricCar(Car):
    def __init__(self, model, year, color, battery):
        Car.__init__(self, model, year, color)
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.__battery = value

    def drive(self):
        print(f'Car {self.model} is driving by electricity')

    def __str__(self):
        return super().__str__() + f' Battery: {self.__battery}'


class FuelCar(Car):
    __total_fuel_amount = 1000

    @staticmethod
    def get_fuel_type():
        return 'AI - 95'

    @classmethod
    def get_total_fuel_amount(cls):
        return cls.__total_fuel_amount

    @classmethod
    def fill_fuel(cls, amount):
        cls.__total_fuel_amount += amount

    def __init__(self, model, year, color, fuel_bank):
        Car.__init__(self, model, year, color)
        self.__fuel_bank = fuel_bank
        FuelCar.__total_fuel_amount -= self.__fuel_bank

    @property
    def fuel_bank(self):
        return self.__fuel_bank

    def drive(self):
        print(f'Car {self.model} is driving by fuel')

    def __str__(self):
        return super().__str__() + f' Fuel Bank: {self.__fuel_bank}'

    def __add__(self, other):
        return self.__fuel_bank + other.__fuel_bank


class HybridCar(FuelCar, ElectricCar):
    def __init__(self, model, year, color, fuel_bank, battery):
        FuelCar.__init__(self, model, year, color, fuel_bank)
        ElectricCar.__init__(self, model, year, color, battery)


some_car = Car('Toyota Camry', 2009, Color.BLUE)
print(some_car)

bmw_car = FuelCar('BMW X5', 2000, Color.SILVER, 70)
print(bmw_car)

tesla_car = ElectricCar('Tesla Model S', 2022, Color.GREEN, 25000)
print(tesla_car)

prius_car = HybridCar('Toyota Prius', 2017, Color.RED, 50, 15000)
print(prius_car)
prius_car.drive()
print(HybridCar.__mro__)

tesla_car.play_music('Song 1')
tesla_car.draw('🚗')

samsung = SmartPhone()
samsung.play_music('Best Song')
samsung.stop_music()
samsung.draw('📱')

num_1 = 9
num_2 = 1
print(f'Number one is bigger than number two: {num_1 > num_2}')
print(f'Number one is better than number two: {bmw_car > prius_car}')
print(bmw_car + prius_car)

# FuelCar.total_fuel_amount-=100
print(f'We have {FuelCar.get_total_fuel_amount()} liters of {FuelCar.get_fuel_type()}.')

FuelCar.fill_fuel(20)
print(f'We have {FuelCar.get_total_fuel_amount()} liters of {FuelCar.get_fuel_type()}.')

if bmw_car.color == Color.SILVER:
    print('This car is beautiful')
