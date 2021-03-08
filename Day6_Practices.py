# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 00:33:38 2021

@author: yesye
"""

# Day 6 - 30DaysOfPython Challenge
# Practices

empty = ()

sisters = ('Ina', 'Rushia')
brothers = ('Angus', 'Izumi')

siblings = sisters + brothers

print('I have', len(siblings) , 'siblings.')

siblings = list(siblings)
siblings.append('Catdy')
siblings.append('Willman')
family_members = tuple(siblings)
print(family_members)

siblings = family_members[0:4]
parents = family_members[4:]

fruits = ('Apple', 'Banana', 'Mango', 'Kiwi')
vegetables = ('Cabbage', 'Peas', 'Lettuce', 'Spinach')
animal_products = ('Pork', 'Beef', 'Watame', 'Pekora')

food_stuff_tp = fruits + vegetables + animal_products

food_stuff_lt = list(food_stuff_tp)
length = len(food_stuff_tp)
if length % 2 == 0:
    middle = food_stuff_tp[length // 2 - 1:length // 2 + 1]
else:
    middle = food_stuff_tp[length // 2 - 1]
print(middle)

first_three = food_stuff_lt[0:3]
last_three = food_stuff_lt[-1:-4:-1]

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)