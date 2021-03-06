# 4.13.3: Greetings
# Korbin Griffin
# 2.5.19

name = input ("What is your name: ")

def greeting():
    print ("Hi there " + name + "!")
    print("Nice to meet you")

greeting()


# 4.13.4: Functions and Variables
# Korbin Griffin
# 2.11.19

x =  10

def print_something():
    x = 3
    print('\r\n', x)

print('\r\n', x)
print_something()


# 4.13.6: Functions and Variables, Part 3
# Korbin Griffin
# 2.18.19


def print_number(x):
    print('\n' + x)

print_number(13)
print_number(23)


# 4.14.4: Name and Age
# Korbin Griffin
# 2.18.19

def name_and_age(name, age):
    print('Hi, my name is', name, 'and I am', str(age), 'years old')

name_and_age('Mike',33)
name_and_age('Zane',18)


# 4.14.5: Default Parameter Values
# Korbin Griffin
# 2.19.19

def print_two_number(x, y = 20):
    print('First number:', x)
    print('Second Number: ' + str(y))

print_two_number(34, 45)
print_two_number(78)

#4.14.6: Print Sum
# Korbin Griffin
# 2.19.19

def print_sum(x, y):
    print(x + y)

print_sum(46, 62)

# 4.16.3: Enter A Number using Try & Except
# Korbin Griffin
# 2.20.19


try:
    my_num = int(input('Enter and integer: '))
    print('Your number:' , my_num)

except ValueError:
    print('That was not an integer!')

try:
    my_num = int(input('Enter and integer: '))
    print('Your number:' , my_num)

except ValueError:
    print('That was not an integer!')

# 4.16.4: Enter Name & Age using the Try and Except Rule
# Korbin Griffin
# 2.20.19

name = input('Enter your name: ')

age = -1

try:
    age = int(input('Enter your age:'))

except ValueError:
    print('n''That was not an integer for your age')

print('\n''Name:', name)
print('Age:', age)


# Korbin Griffin
# 1.14.19



my_number = 10

print ("Guess a number between 1 and 10")
print("")

guess = int(input("Enter a guess: "))

while guess != my_number:
    print ("Wrong, guess again")
    guess = int(input("Enter a guess: "))

print("")

print ("Good job, you got it!")

# Program Tracing
# Korbin Griffin

x = 10

while x > 5:
    print (x)
    x = x - 2
