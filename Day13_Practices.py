# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 12:59:42 2021

@author: yesye
"""
# Day 13 - 30DaysOfPython Challenge
# Practices

#Q1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negatives = [number for number in numbers if number <= 0]
print(negatives)

#Q2
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
_list = [i for row in list_of_lists for j in row for i in j]
print(_list)

#Q3
power = [(i, i ** 0, i ** 1, i ** 2, i ** 3, i ** 4, i ** 5) for i in range(11)]

#Q4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
nordic = [(country.upper()) for row in countries for _tuple in row for country in _tuple]

#Q5
capital = [{'country': _tuple[0].upper(), 'city':_tuple[1].upper()} for row in countries for _tuple in row]

#Q6
names = [[('Asabeneh', 'Yetaeyeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
name_list = [(name[0] + ' ' + name[1]) for row in names for name in row]

#Q7
slope = lambda x1, y1, x2, y2: (y2-y1)/(x2-x1)
print(slope(0, 0, 1, 1))