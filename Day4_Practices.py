# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 15:10:15 2021

@author: yesye
"""

# Day 4 - 30DaysOfPython Challenge
# Practices

#Q1-8

string1 = 'Thirty' + ' Days' + ' Of' + ' Python'
company = 'Coding' + ' For' + ' All'

print(string1)
print(company)

print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())

#Q9
_slice = company.split(' ',1)[0]
print(_slice)

#Q10
print(company.find('Coding')!= -1)

#Q11
print(company.replace('Coding', 'Python'))

#Q12
print('Python for Everyone'.replace('Everyone','All'))

#Q13
_slices = company.split(' ')
print(_slices)

#Q14
q14 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
_split = q14.split(', ')
print(_split)

#Q15-17
print(company[0], company[-1], company[10])

#Q18
q18 = 'Python For Everyone'
_split2 = q18.split()
acronym1 = ''
for i in range(len(_split2)):
    acronym1 += _split2[i][0]
print(acronym1)

#Q19
q19 = 'Coding For All'
_split3 = q19.split()
acronym2 = ''
for i in range(len(_split3)):
    acronym2 += _split3[i][0]
print(acronym2)

#Q20-21
print(company.index('C'), company.index('F'))

#Q22
q22 = company + ' People'
print(q22.rindex('l'))

#Q23-25
q2324 = 'You cannot end a sentence with because because because is a conjunction'

print(q2324.find('because'), q2324.rindex('because'))
start = q2324.find('because') - 1
end = q2324.rindex('because') + len('because')

newstring = q2324[:start] + q2324[end:]
print(newstring)

#Q28-29
print(company.startswith('Coding'))
print(company.endswith('coding'))

#Q30
q30 = '   Coding For All      ' 
ans = q30.strip()
print(ans)

#Q31
q31_1 = '30DaysOfPython'
q31_2 = 'thirty_days_of_python'

if q31_1.isidentifier():
    print('The first one is correct')
elif q31_2.isidentifier():
    print('The second one is correct')
elif q31_1.isidentifier() and q31_2.isidentifier():
    print('Both are correct')
else:
    print('Both are incorrect.')
    
#Q32
q32 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
combine_q32 = '# '.join(q32)
print(combine_q32)

#Q33
print('I am enjoying this challenge.\nI just wonder what is next.')

#Q34
print('Name\tAge\tCountry')
print('Asabeneh\t250\tFinland')

#Q35
radius = 10
area = 3.14 * radius ** 2
formatted = 'The area of a circle with radius {} is {} meters square'.format(radius, area)
print(formatted)

#Q36
num1 = 8
num2 = 6

print('{} + {} = {}'.format(num1,num2,num1+num2))
print('{} - {} = {}'.format(num1,num2,num1-num2))
print('{} * {} = {}'.format(num1,num2,num1*num2))
print('{} / {} = {:.2f}'.format(num1,num2,num1/num2))
print('{} % {} = {}'.format(num1,num2,num1%num2))
print('{} // {} = {}'.format(num1,num2,num1//num2))
print('{} ** {} = {}'.format(num1,num2,num1**num2))
