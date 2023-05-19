from random import randint as generate_number, choice
import calculator
from person import Person
from termcolor import cprint
import emoji
from decouple import config

print(generate_number(2, 5))
print(choice([2, 3, 4, 5, 6, 7, 8, 8, 9]))

print(calculator.addition(8, 3))

my_friend = Person('Jim', 33)
print(my_friend)

cprint("Hello, World!", "green", "on_red")
print(emoji.emojize('Python is :thumbs_up:'))

print(config('DATABASE_URL'))

num = config('COMMENTED', default=9, cast=int)
print(num * 2)
