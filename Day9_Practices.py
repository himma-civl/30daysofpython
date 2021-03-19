# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 13:16:59 2021

@author: yesye
"""

# Day 9 - 30DaysOfPython Challenge
# Practices

#Q1
age = int(input('Enter your age: '))
print('You are old enough to drive') if age >= 18 else print('You need', 18-age, 'more years to learn to drive.')

#Q2
my_age = 21
your_age = int(input('Enter your age: '))
age_diff = abs(my_age - your_age)

if my_age > your_age:
    if age_diff == 1:
        print('I am 1 year older than you.')
    else:
        print('I am',age_diff,'years older than you.')
elif my_age < your_age:
    if age_diff == 1:
        print('You are 1 year older than me.')
    else:
        print('You are',age_diff,'years older than me.')
elif my_age == your_age:
    print('We are equally old.')

#Q3
num1 = int(input('Enter number one: '))
num2 = int(input('Enter number two: '))

if num1 > num2:
    print(f'{num1} is greater than {num2}.')
elif num1 < num2:
    print(f'{num1} is smaller than {num2}.')
else:
    print(f'{num1} and {num2} are equal.')

#Q4
score = int(input('Enter the score: '))
if score >= 0:
    if score >= 80 and score <= 100:
        print('Grade: A')
    elif score >= 70 and score <= 79:
        print('Grade: B')
    elif score >= 60 and score <= 69:
        print('Grade: C')
    elif score >= 50 and score <= 59:
        print('Grade: D')
    else:
        print('Grade: F')
else:
    print('Invalid score, please enter again.')
    
#Q5
month = input('Enter a month: ').capitalize()
spring = ('March','April','May')
summer = ('June','July','August')
autumn = ('September','October','November')
winter = ('January','February','December')
if month in spring:
    print('This month is in Spring.')
elif month in summer:
    print('This month is in Summer.')
elif month in autumn:
    print('This month is in Autumn.')
elif month in winter:
    print('This month is in Winter.')
else:
    print('Invalid input.')
    
#Q6
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Enter a fruit: ').lower()
if fruit in fruits:
    print('That fruit already exist in the list.')
else:
    fruits.append(fruit)
    print(fruits)

#Q7
person={
'first_name': 'Izumi',
'last_name': 'Kun',
'age': 21,
'country': 'Hong Kong',
'is_married': False,
'skills': ['Python', 'VISSIM', 'Excel', 'Writing'],
'address': {
    'street': 'Kwong Fuk Road',
    'zipcode': 'N/A'
}
}
key = list(person.keys())

if 'skills' in key:
    middle = divmod(len(person['skills']), 2)
    if middle[1] == 0:
        print(person['skills'][middle[0] - 1:middle[0] + 1])
    else:
        print(person['skills'][middle[0]])
    
    if 'Python' in person['skills']:
        print('Python is in skills')
    else:
        print('Python is not in skills')

'''
If a person skills has only JavaScript and React, 
print('He is a front end developer'), 
if the person skills has Node, Python, MongoDB, 
print('He is a backend developer'), 
if the person skills has React, Node and MongoDB, 
print('He is a fullstack developer'), 
else 
print('unknown title') 
- for more accurate results more conditions can be nested!
'''

if person['is_married'] == False and person['country'] == 'Hong Kong':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is not married.")
