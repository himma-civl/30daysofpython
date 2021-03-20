# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 14:54:30 2021

@author: yesye
"""

# Day 11 - 30DaysOfPython Challenge
# Practices
import math
import keyword

#Q1
def add_two_numbers(num1, num2):
    _sum = num1 + num2
    return _sum

#Q2
def area_of_circle(r):
    area = r ** 2 * math.pi
    return area

#Q3
def convert_celcius_to_fahrenheit(temperature_C):
    temperature_F = (temperature_C * 9/5) + 32
    return temperature_F

#Q4
def add_all_sum(*nums):
    _sum = 0
    for num in nums:
        _sum += num
    return _sum

#Q5
def check_season(month):
    spring = ('March','April','May')
    summer = ('June','July','August')
    autumn = ('September','October','November')
    winter = ('January','February','December')
    Month = month.capitalize()
    if Month in spring:
        season = 'Spring'
    elif Month in summer:
        season = 'Summer'
    elif Month in autumn:
        season = 'Autumn'
    elif Month in winter:
        season = 'Winter'
    else:
        season = 'Invalid input'
    return season

#Q6
def calculate_slope(point1, point2):
    slope = (point2[1]-point1[1])/(point2[0]-point1[0])
    return slope

#Q7
def solve_quadratic_eqn(a = 0, b = 0, c = 0):
    discriminant = b ** 2 - 4 * a * c
    solutions = []
    if discriminant > 0:
        sol1 = (-b + math.sqrt(discriminant)) / (2 * a)
        sol2 = (-b - math.sqrt(discriminant)) / (2 * a)
        solutions.extend([sol1, sol2])
    elif discriminant == 0:
        sol = (-b + math.sqrt(discriminant)) / (2 * a)
        solutions.append(sol)
    else:
        solutions.append('No real roots')
    return solutions

#Q8
def print_list(_list):
    for item in _list:
        print(item)

#Q9
def reverse_list(_list):
    tsil_ = []
    while len(_list) != 0:
        temp = _list.pop()
        tsil_.append(temp)
    return tsil_

#Q10
def capitalize_list_items(_list):
    for i in range(len(_list)):
        _list[i] = _list[i].capitalize()
    return _list

#Q11
def add_item(_list, item):
    _list.append(item)
    return _list

#Q12
def remove_item(_list, item):
    if item in _list:
        _list.remove(item)
    else:
        print('Item not found. No item is removed.')
    return _list

#Q13
def sum_of_numbers(num):
    _sum = 0
    for i in range(num+1):
        _sum += i
    return _sum

#Q14
def sum_of_odds(num):
    _sum = 0
    for i in range(num+1):
        if i % 2 == 1:
            _sum += i
    return _sum

#Q15
def sum_of_evens(num):
    _sum = 0
    for i in range(num+1):
        if i % 2 == 0:
            _sum += i
    return _sum

#Q16
def evens_and_odds(num):
    evens = 0
    odds = 0
    for i in range(num+1):
        if i % 2 == 0:
            evens +=1
            continue
        odds += 1
    print(f'The number of odds are {odds}')
    print(f'The number of evens are {evens}.')
 
#Q17
def factorial(num):
    fac = 1
    for i in range(1,num+1):
        fac *= i
    return fac

#Q18 #not handling collection and other newly introduced data type
def is_empty(item):
    _empty = False
    if type(item) is not int and type(item) is not float and type(item) is not complex:
        if len(item) == 0:
            _empty = True
    return _empty

#Q19
def calculate_mean(_list):
    mean = sum(_list)/len(_list)
    return mean

def calculate_median(_list):
    _list.sort()
    if len(_list) % 2 == 1:
        median = _list[len(_list) // 2]
    else:
        median = (_list[len(_list) // 2 - 1] + _list[len(_list) // 2]) / 2
    return median

def calculate_mode(_list):
    unique_item = set(_list)
    mode = 0
    mode_count = 1
    for item in unique_item:
        count = _list.count(item)
        if count > mode_count:
            mode_count = count
            mode = item
    return mode

def calculate_range(_list):
    _max = max(_list)
    _min = min(_list)
    _range = _max - _min
    return _range

#population var/std, not sample var/std
def calculate_variance(_list):
    mean = calculate_mean(_list)
    deviation = 0
    for item in _list:
        deviation += (item - mean) ** 2
    variance = deviation / len(_list)
    return variance

def calculate_std(_list):
    std = math.sqrt(calculate_variance(_list))
    return std

#Q20 #RUN TIME IS A PROBLEM
def is_prime(num):
    is_prime = True
    for i in range(2, num // 2):
        if num % i == 0:
            is_prime = False
            break
    return is_prime

#Q21
def all_unique(_list):
    unique = True
    temp = set(_list)
    if len(temp) != len(_list):
        unique = False
    return unique

#Q22
def same_type(_list):
    same = True
    type1 = ''
    type2 = ''
    for i in range(1,len(_list)):
        type1 = type(_list[i-1])
        type2 = type(_list[i])
        if type1 != type2:
            same = False
            break
    return same

#Q23 #lack checking of built-in functions
def variable_check(name):
    valid = True
    num = []
    for i in range(10):
        num.append(str(i))
    uppercase = []
    for j in range(65,91):
        uppercase.append(chr(j))
    lowercase = []
    for k in range(97,123):
        lowercase.append(chr(k))
    _keyword = keyword.kwlist
    
    if (name[0] != '_') and (name[0] not in uppercase) and (name[0] not in lowercase):
        valid = False
    
    if name in _keyword:
        valid = False
    
    if valid:
        for character in name[1:]:
            if (character not in num) and (character not in uppercase) \
                and (character not in lowercase) and (character != '_'):
                    valid = False
                    break
    
    return valid

print(keyword.kwlist)
test_list = ['angus','izumi','ina','ame','rushia']
test_list_2 = [1,3,2,4,5,6,7,9]
test_list_3 = test_list + test_list_2
test_list_4 = [1,2,3,1]
print(add_two_numbers(2, 3))
print(area_of_circle(5))
print(convert_celcius_to_fahrenheit(36))
print(add_all_sum(2,4,5,100))
print(check_season('march'))
print(calculate_slope((0,0), (3,2)))
print(solve_quadratic_eqn(1,-5,2))
print_list(test_list)
print(reverse_list(test_list))
print(capitalize_list_items(test_list))
print(add_item(test_list,'nene'))
print(remove_item(test_list, 'Angus'))
print(sum_of_numbers(100))
print(sum_of_odds(100))
print(sum_of_evens(100))
evens_and_odds(100)
print(factorial(6))
print(calculate_mean(test_list_2))
print(calculate_median(test_list_2))
print(calculate_mode(test_list_2)) #returns 0 when no mode is find
print(calculate_range(test_list_2))
print(calculate_variance(test_list_2))
print(calculate_std(test_list_2))
print(is_prime(1000003))
print(all_unique(test_list_3))
print(all_unique(test_list_4))
print(same_type(test_list))
print(same_type(test_list_3))
print(variable_check('_sum'))
print(variable_check('sum'))
print(variable_check('1zumi'))
print(variable_check('sAsaA'))

