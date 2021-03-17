# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 18:03:51 2021

@author: yesye
"""

# Day 8 - 30DaysOfPython Challenge
# Practices

dog = {}
dog['name'] = 'Inugami Korone'
dog['color'] = 'brown'
dog['breed'] = 'Cavalier King Charles Spaniel'
dog['legs'] = 2
dog['age'] = 90

print(dog)
print(dog.get('name'))

student = {
    'frist_name' : 'Izumi',
    'last_name' : 'N/A',
    'gender' : 'Male',
    'age' : 21,
    'is_married' : False,
    'skills' : ['Python','Writing','Photography','VISSIM'],
    'country' : 'Hong Kong',
    'city' : 'Tuen Mun',
    'address' : 'placeholder'}

print(student)

print(len(student))

print(student.get('skills'))
print(student['skills'])
print(type(student['skills']))

student['skills'].extend(['Excel','English'])
print(student['skills'])

_key = list(student.keys())
print(_key)

_value = list(student.values())
print(_value)

_item = tuple(student.items())
print(_item)
print(type(_item))

del student['address']
student.pop('is_married')
student.popitem()
del dog