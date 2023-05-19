class Transport:
    def __init__(self, the_model, the_year, the_color):
        # attributes/fields
        self.model = the_model
        self.year = the_year
        self.color = the_color

    def change_color(self, new_color):
        self.color = new_color


class Plane(Transport):
    def __init__(self, the_model, the_year, the_color):
        # attributes/fields
        super().__init__(the_model, the_year, the_color)


class Car(Transport):
    #class attributes
    number_of_wheels = 4
    counter = 0

    # constructor
    def __init__(self, the_model, the_year, the_color, penalties=0.0):
        # attributes/fields
        super().__init__(the_model, the_year, the_color)
        self.penalties = penalties
        Car.counter += 1

    # method
    def drive(self, city):
        print(f'Car {self.model} is driving to {city}')

    def make_signal(self, number_of_times):
        beeps = 'BEEP ' * number_of_times
        print(f'Car {self.model} {beeps}')


class Truck(Car):
    number_of_wheels = 6
    def __init__(self, the_model, the_year, the_color, penalties=0.0, load_capacity=0):
        super().__init__(the_model, the_year, the_color, penalties)
        self.load_capacity = load_capacity

    def load_cargo(self, type, weight):
        if weight > self.load_capacity:
            print(f'You can not load more than {self.load_capacity} kg')
        else:
            print(f'You successfully loaded {type} of weight {weight} kg on {self.model}')


print(f'We need {Car.number_of_wheels * 10 * 5000} soms to buy summer lastics')

bmw_car = Car('BMW X7', 2020, 'Red')
print(bmw_car)
print(f'Model: {bmw_car.model} Year: {bmw_car.year} Color: {bmw_car.color} Penalties: {bmw_car.penalties}')

honda_car = Car(the_year=2009, the_color='White', the_model='Honda Fit', penalties=900)
print(f'Model: {honda_car.model} Year: {honda_car.year} Color: {honda_car.color} Penalties: {honda_car.penalties}')

# honda_car.color = 'Red'
honda_car.change_color('Red')
print(f'Model: {honda_car.model} Year: {honda_car.year} NEW Color: {honda_car.color} Penalties: {honda_car.penalties}')
honda_car.drive('Osh')
bmw_car.drive('Tokmok')
bmw_car.make_signal(5)

print(f'We produced {Car.counter} cars.')

boeing_plane = Plane('Boeing 747', 2022, 'Silver')
print(f'Model: {boeing_plane.model} Year: {boeing_plane.year} Color: {boeing_plane.color}')

zil_truck = Truck('Zil 130', 1987, 'Blue', 1200, 8000)
zil_truck.load_cargo('Apples', 10000)
zil_truck.load_cargo('Apples', 5000)
zil_truck.drive('Kant')


print(f'We need {Truck.number_of_wheels * 10 * 5000} soms to buy summer lastics TRUCK')