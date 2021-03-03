# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 13:41:30 2021

@author: yesye
"""

# Day 3 - 30DaysOfPython Challenge
# Practices
import math
#Q1 - Q3
age = 21
height = 170.4
_complex = 1 + 1j #remember use j as complex no..

#Q4
base = float(input('base: '))
height = float(input('height: '))
areaoftriangle = 0.5 * base * height
print('The area of the triangle is', areaoftriangle)

#Q5
a = float(input('side a: '))
b = float(input('side b: '))
c = float(input('side c: '))
perimeteroftriangle = a + b + c
print('The perimeter of the triangle is', perimeteroftriangle)

#Q6
length = float(input('length: '))
width = float(input('width: '))
areaofrectangle = length * width
perimeterofrectangle = 2 * (length + width)
print('The are of the rectangle is',areaofrectangle)
print('The perimeter of the rectangle is',perimeterofrectangle)

#Q7
radius = float(input('radius: '))
areaofcircle = math.pi * radius ** 2
circumference = 2 * math.pi * radius
print('The area of the circle is', areaofcircle)
print('The circumference of the circle is ', circumference)
print()
#Q8
#x intercept
y = 0
X = (y + 2) / 2

#y intercept
x = 0 
Y = 2 * x - 2

#slope
M = (y - Y) / (X - x)

print('x-intercept:', X)
print('y-intercept:', Y)
print('slope:', M)
print()
#Q9
x1, y1 = 2, 2
x2, y2 = 6, 10

m = (y2 - y1) / (x2 - x1)
print('point 1:(',x1,',',y1,')')
print('point 2:(',x2,',',y2,')')
print('slope:',m)
print()
#Q10
if M > m:
    print('slope 1 is steeper.')
elif m > M:
    print('slope 2 is steeper.')
else:
    print('The two slopes are equal.')
    
print()

#Q11
A = 1
B = 6
C = 9

X1 = (-B + (B ** 2 - 4 * A * C) ** 0.5) / (2 * A)
X2 = (-B - (B ** 2 - 4 * A * C) ** 0.5) / (2 * A)

print('Solution of ', A, 'x^2+', B, 'x+', C, 'is', X1, 'and', X2)

#Q12
_str1 = 'python'
_str2 = 'jargon'

print('Q12:', not(len(_str1) == len(_str2)))
print()

#Q13
print('Q13:', 'on' in _str1 and 'on' in _str2)
print()

#Q14
quote = 'I hope this course is not full of jargon'
print('Q14', _str2 in quote)
print()

#Q15
_str3 = 'dragon'
print('Q15', not('on' in _str3 and 'on' in _str1))
print()

#Q16
len_str1 = str(float(len(_str1)))
print(len_str1)
print(type(len_str1))
print()

#Q17
num = int(input('Input an integer: '))
if (num % 2) == 0:
    print('This number is an even number.')
else:
    print('This number is an odd number.')
print()

#Q18-20
print('Q18', (7//3) == int(2.7))
print()
print('Q19', type('10') == 10)
print()
#print('Q20', int('9.8') == 10) #potential error in Q20


#Q21
print('Q21: ')
hour = int(input('Enter hours (as integer): '))
rate = int(input('Enter rate per hour (as integer): '))
earning = hour * rate
print('Your weekly earning is', earning)
print() 

#Q22
print('Q22: ')
year_lived = int(input('Enter number of years you have lived (in integer): '))
second_lived = year_lived * 365 * 24 * 60 * 60
print('You have lived for',second_lived,'seconds.')
print()

#Q23 with loops
print('Q23: ')
for x in range(1, 6, 1):
    print(x, end = ' ')
    for y in range(4):
        print(x ** y, end = ' ')
    print()
