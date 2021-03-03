# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 16:01:01 2021

@author: yesye
"""
# Day 2 - 30DaysOfPython Challenge
# Practices
import math

"""
Exercises: Level 1
1. Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
2. Write a python comment saying 'Day 2: 30 Days of python programming'
3. Declare a first name variable and assign a value to it
4. Declare a last name variable and assign a value to it
5. Declare a full name variable and assign a value to it
6. Declare a country variable and assign a value to it
7. Declare a city variable and assign a value to it
8. Declare an age variable and assign a value to it
9. Declare a year variable and assign a value to it
10. Declare a variable is_married and assign a value to it
11. Declare a variable is_true and assign a value to it
12. Declare a variable is_light_on and assign a value to it
13. Declare multiple variable on one line

Exercises: Level 2
1. Check the data type of all your variables using type() built-in function
2. Using the len() built-in function find the length of your first name
3. Compare the length of your first name and your last name
4. Declare 5 as num_one and 4 as num_two
    i. Add num_one and num_two and assign the value to a variable _total
    ii. Subtract num_two from num_one and assign the value to a variable _diff
    iii. Multiply num_two and num_one and assign the value to a variable _product
    iv. Divide num_one by num_two and assign the value to a variable _division
    v. Use modulus division to find num_two divided by num_one and assign the value to a variable _remainder
    vi. Calculate num_one to the power of num_two and assign the value to a variable _exp
    vii. Find floor division of num_one by num_two and assign the value to a variable _floor_division
5. The radius of a circle is 30 meters.
    i. Calculate the area of a circle and assign the value to a variable area_of_circle
    ii. Calculate the circumference of a circle and assign the value to a variable circum_of_circle
    iii. Take radius as user input and calculate the area.
6. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
7. Run help('keywords') in python shell or in your file to check for the reserved words
"""

# Level 1
# Day 2: 30 Days of python programming
first_name = 'Angus'
last_name = 'Chang'
name = first_name + '' + last_name
country = 'Hong Kong'
city = 'Tuen Mun'
age = 21
year = 2021
is_married = False
is_true = True
is_light_on = False

var1, var2, var3, var4 = 1,2,3,4

#Level 2
print(type(first_name))
print(type(last_name))
print(type(name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))    

len_first_name = len(first_name)
len_last_name = len(last_name)

print('Length of first name is ', len_first_name)
print('Length of last name is', len_last_name)

if len_first_name > len_last_name:  
    print('First name is longer than last name')
elif len_last_name < len_first_name:
    print('Last name is longer than first name')
else:
    print('Both First name and last name has the same length')

num_one, num_two = 5, 4
_total = num_one + num_two
_diff = num_one - num_two
_product = num_one * num_two
_division = num_one / num_two
_remainder = num_one % num_two
_exp = num_one ** num_two
_floor_division = num_one // num_two

print('Sum of', num_one, 'and', num_two, 'is', _total, '.')
print('Difference of', num_one, 'and', num_two, 'is', _diff, '.')
print('Product of', num_one, 'and', num_two, 'is', _product, '.')
print('The result of', num_one, 'divided by', num_two, 'is', _division, '.')
print('The Remainder of', num_one, 'divided by', num_two, 'is', _remainder,'.')
print(num_one, 'to the power of', num_two, 'is', _exp, '.')
print('The quotient of', num_one, 'and', num_two, 'is', _floor_division, '.')

radius = 30
area_of_circle = math.pi * (radius ** 2)
circum_of_circle = 2 * math.pi * radius
print('The area of the circle is ', area_of_circle,'.')
print('The circumference of the circle is', circum_of_circle,'.')
print('Circle area calculator')
Radius = float(input('Please input the radius of the circle: ')) 
# Remember input() take input as string, so a type change is needed. 
# float to tackle not just radius in integer
Area_of_circle = math.pi * (Radius**2)
print('The area of the circle is', Area_of_circle, '.')

print('Welcome to my first Python program!!')
print('How are you? Nice to meet you!')
print('Would you like to introduce yourself a little bit?')
First_name = input("What's your first name? : ")
Last_name = input("What's your last name? : ")
Country = input("Which country do you come from? ")
Age = input("How old are you? :") 
# Type check should exists in all cases, but for now I would ignore it cause I am still relearning
    
print('So you are', First_name, Last_name, '?')
print('And you are', Age, 'years old?')
print('And you came from', Country, '?')
print('Nice to meet you! I am',first_name, last_name,'!')
print('I come from', country)
print('And I am', age, 'years old.')
print('Have a nice day my friend!')

