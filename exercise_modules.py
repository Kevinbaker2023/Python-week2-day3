import math

def square_footage():
    length = int(input('What is the length of your house?'))
    width = int(input('What is the width of your house?'))
    area = length * width
    return f'The area of your house is {area} square feet.'

def circumference():
    while True:
        question = input('Do you have the diameter or radius')
        if question == 'diameter':
            diameter = int(input('What is the diameter?'))
            half = diameter / 2
            return 2 * math.pi * half
        elif question == 'radius':
            radius = int(input('What is the radius?'))
            return 2 * math.pi * radius
        elif question != 'diameter' and question != 'radius':
            print('That is not an accepted input, please try again.')