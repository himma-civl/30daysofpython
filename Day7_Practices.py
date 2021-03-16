# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 22:37:44 2021

@author: yesye
"""

# Day 7 - 30DaysOfPython Challenge
# Practices

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
it_companies.update(['Samsung','Intel','AMD'])
it_companies.remove('Facebook')
it_companies.discard('Facebook')

ANB = A.union(B)
print(ANB)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.symmetric_difference(B))

#del it_companies, A, ANB, B

age_set = set(age)
print(age_set)

print(len(age))
print(len(age_set))


Q15 = 'I am a teacher and I love to inspire and teach people.'
unique_word = set(Q15)
print(len(unique_word))
