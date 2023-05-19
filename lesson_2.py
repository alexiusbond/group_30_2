class Contacts:
    def __init__(self, city, street, number):
        self.__city = city
        self.__street = street
        self.__number = number

    @property
    def city(self):
        return self.__city

    @property
    def street(self):
        return self.__street

    @property
    def number(self):
        return self.__number


class Animal:
    def __init__(self, name, age, contacts):
        self.__name = name
        if isinstance(age, int) and age > 0:
            self.__age = age
        else:
            raise ValueError('Wrong value for attribute age, '
                             'it must be positive number')
        if isinstance(contacts, Contacts):
            self.__contacts = contacts
        else:
            raise ValueError('Wrong value for attribute contacts, '
                             'it must be of data type Contacts')
        self.__was_born()

    def __was_born(self):
        print(f'Animal {self.__name} was born!')

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if isinstance(new_age, int) and new_age > 0:
            self.__age = new_age
        else:
            raise ValueError('Wrong value for attribute age, '
                             'it must be positive number')

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def info(self):
        return f'Name: {self.__name} Age: {self.__age} ' \
               f'Birth Year: {2023 - self.__age}\n' \
               f'ADDRESS: {self.__contacts.city}, {self.__contacts.street} ' \
               f'{self.__contacts.number}'

    def speak(self):
        raise NotImplementedError('Method speak() must be implement')


class Fish(Animal):
    def __init__(self, name, age, contacts):
        super(Fish, self).__init__(name, age, contacts)

    def speak(self):
        pass

class Cat(Animal):
    def __init__(self, name, age, contacts):
        super(Cat, self).__init__(name, age, contacts)

    def speak(self):
        print('Myauuu')


class Dog(Animal):
    def __init__(self, name, age, commands, contacts):
        super(Dog, self).__init__(name, age, contacts)
        self.__commands = commands

    @property
    def commands(self):
        return self.__commands

    @commands.setter
    def commands(self, value):
        self.__commands = value

    def info(self):
        return super().info() + f'\nCommands: {self.__commands}'

    def speak(self):
        print('Gaaav')


class FightingDog(Dog):
    def __init__(self, name, age, commands, wins, contacts):
        super(FightingDog, self).__init__(name, age, commands, contacts)
        self.__wins = wins

    @property
    def wins(self):
        return self.__wins

    @wins.setter
    def wins(self, value):
        self.__wins = value

    def info(self):
        return super().info() + f'\nWins: {self.wins}'


# a       = b
contact_1 = Contacts('Bishkek', 'Toktogula', 103)

# some_animal = Animal('Anim', 2, contact_1)
# some_animal.__age = 'Four years old'
# some_animal.set_age(3)
# print(some_animal.info())
# print(some_animal.get_name())

dog = Dog('Snooppy', 5, 'Sit', contact_1)
dog.commands = 'Sit, run'
print(dog.commands)

cat = Cat('Tom', 9, Contacts('Osh', 'Masalieva', 2))

fighting_dog = FightingDog('Reks', 1, 'Fight', 10, contact_1)

fish = Fish('Nemo', 1, contact_1)
animals_list = [dog, cat, fish, fighting_dog]
for animal in animals_list:
    animal.speak()
    print(animal.info())
