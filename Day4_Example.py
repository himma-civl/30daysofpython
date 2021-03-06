# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 15:07:46 2021

@author: yesye
"""
# Day 4 - 30DaysOfPython Challenge
# Examples
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""

print(multiline_string)

#tab function check: Tab display width is depending on IDE
test = 'I\thate\tthis'
print(test)
print(test.expandtabs())

test2 = "\""

print(test2)

language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto

test3 = 'sdjbjdfhjhj\tkjshdklshdskhdkh'
print(test3)
print(test3.expandtabs(8))

#that's why we got different display than GitHub webpage
print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"')

#string.format() and f-string
name = 'Izumi'
age = 21
test4 = 'My name is {} and I am {} years old.'.format(name, age)
print(test4)
test5 = f'My name is {name} and I am {age} years old.'
print(test5)

first_letter = name[0]
print(first_letter)

#find and index
test6 = test4.find('name')
test61 = test4.index('name')
test7 = test4.rfind('name')
test71 = test4.rindex('name')

print(test6, test61, test7, test71)


#strip
challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth')) 
test8 = '       myy       '
print(test8.strip(' y'))


print(test6, test7)

challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']

