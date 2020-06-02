# Basics of Python Tutorial:
# https://www.youtube.com/watch?v=UsCQXe1OHZk&list=PLQVvvaa0QuDe8XSftW-RAxdo6OmaeL85M&index=4&t=0s

print('This is an example of print function')

print("we're going to the store")

print("Hi!")

print('We\'re going to the store')

print('Hi', 'there')

print('Hi', 5)

# print('Hi'+ 5)
# print(5+'Hi')

print('Hi ' + str(5))

print('8' + str(5))

# print(int('8.5')+5)
# 8.5 is not integer, so use float

print(float('8.5') + 5)

#   + - * /

print(1 + 3)

print(4 * 4)

print(25 / 5)

print(5 / 34)

print(4 ** 4)

# Variables

exampleVar = 55 + 32
print(exampleVar)

exampleVar = print('whoo')

x, y = (3, 5)

print(x)
print(y)

# While loop

condition = 1

while condition < 10:
    print(condition)
    condition += 1
# condition = condition +1


# while True:
# print('doing stuff')

# for loop

exampleList = [1, 5, 6, 1, 6, 7, 8, 9, 345, 53, 5]

for eachNumber in exampleList:
    print(eachNumber)
    print('continue program')

for x in range(1, 11):
    print(x)

# If statement:
# https://www.youtube.com/watch?v=4u2ClNCtcgY&list=PLQVvvaa0QuDe8XSftW-RAxdo6OmaeL85M&index=8

x = 5
y = 8
z = 5
a = 3

# if x > y:
# print('x is greater than y')

# if x < y:
# print('x is less than y')

# if z < y > x > a:
# print('y is greater than z and greater than x')

# if z <= x:
# print ('z is less than or equal to x')

if z == x:
    print('z is equal to x')

if z != x:
    print('z is not equal to y')

if z != y:
    print('z is not equal to y')

# else statement:
# https://www.youtube.com/watch?v=qf0sfRZ0hHc&list=PLQVvvaa0QuDe8XSftW-RAxdo6OmaeL85M&index=9

x = 5
y = 8

if x > y:
    print('x is greater than y')
if x < 55:
    print('x is greater than 55')
else:
    print('x is not greater than y')

# if elif else:    *elif = else if
# https://www.youtube.com/watch?v=42MBMSOZgD4&list=PLQVvvaa0QuDe8XSftW-RAxdo6OmaeL85M&index=10

x = 5
y = 10
z = 22

if x > y:
    print('s is greater than y')
elif x == z:
    print('x is < than z')
elif 5 == 2:
    print('5 is greater than 2')
else:
    print('if and elif(s) never ran')


# Basic of Function:
# https://www.youtube.com/watch?v=owglNL1KQf0&list=PLQVvvaa0QuDe8XSftW-RAxdo6OmaeL85M&index=11

def example():
    print('basic function')
    z = 3 + 9
    print(z)


example()


# Function Parameters
# https://www.youtube.com/watch?v=CGRKqnoQGgM&list=PLQVvvaa0QuDe8XSftW-RAxdo6OmaeL85M&index=12

def simple_addition(num1, num2):
    answer = num1 + num2
    print('num1 is', num1)
    print(answer)

simple_addition(5,3)

# Function Parameters Defaults
# https://www.youtube.com/watch?v=KeRxe9rll2Q&list=PLQVvvaa0QuDe8XSftW-RAxdo6OmaeL85M&index=13

def simple(num1, num2):
    pass

def simple(num1, num2=5):
    print(num1, num2)

simple(2)

def basic_window(width, height, font='TNR',
                 bgc='w', scrollbar=True):
    print(width, height, font, bgc)

basic_window(500, 350,bgc='b')

# Global and Local Variables
# https://www.youtube.com/watch?v=r9LtArXOYjk&list=PLQVvvaa0QuDe8XSftW-RAxdo6OmaeL85M&index=14

# this is not global valuable

x = 6

def example():
    '''z = 5
    print(z)'''

    globx = x
    print(globx)
    globx+=5

example()




