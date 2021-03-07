# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 18:42:59 2021

@author: yesye
"""

# Day 5 - 30DaysOfPython Challenge
# Practices

_list = []
LEC = ['G2','FNC','RGE','MAD','SK','MSF','XL','AST','VIT','S04']
print(len(LEC))

first_item = LEC[0]
last_item = LEC[-1]
middle_item = LEC[len(LEC)//2]

print(first_item, last_item, middle_item)

it_companies = ['Facebook', 'Google', 'Microsoft','Apple','IBM', 'Oracle','Amazon']
print(it_companies)

print(len(it_companies))

print(it_companies[0],it_companies[len(it_companies)//2],it_companies[-1])

it_companies[0] = 'Fuckbook'
print(it_companies)

it_companies.append('Samsung')
print(it_companies)

it_companies.insert(len(it_companies)//2, 'Intel')
print(it_companies)

it_companies[1] = it_companies[1].upper()
print(it_companies)

IT = '#; '.join(it_companies)
print(IT)

print(it_companies.index('Fuckbook'))

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

_slice1 = it_companies[0:3]
_slice2 = it_companies[-1:-4:-1]
print(_slice1)
print(_slice2)

_slice3 = []
for i in range(len(it_companies)):
    if not(it_companies[i] in _slice1) and not(it_companies[i] in _slice2):
        _slice3.append(it_companies[i])
print(_slice3)

del it_companies[0]
print(it_companies)
del it_companies[len(it_companies)//2]
print(it_companies)
del it_companies[-1]
print(it_companies)
it_companies.clear()
print(it_companies)
del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

join = front_end + back_end
print(join)

full_stack = join.copy()
index = full_stack.index('Redux')
full_stack.insert(index + 1, 'Python')
full_stack.insert(index + 2, 'SQL')
print(full_stack)

#lv2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
minage = ages[0]
maxage = ages[-1]
print(minage, maxage)

length = len(ages)
if length % 2 == 0:
    medianage = (ages[int(len(ages)/2)-1] + ages[int(len(ages)/2)])/2
else:
    medianage = ages[len(ages)//2]
print(medianage)

avgage = sum(ages)/len(ages)
print(avgage)

_range = maxage - minage
print(_range)

print(abs(minage - avgage) > abs(maxage - avgage))

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];

len_list = len(countries)
middle = []
if len_list % 2 == 0:
    middle = countries[len(countries)//2 - 1:len(countries)//2 + 1]
else:
    middle = countries[len(countries)//2]
print(middle)

list1, list2 = [], []

if len_list % 2 == 0:
    list1 = countries[0:len_list // 2]
    list2 = countries[len_list//2:]
else:
    list1 = countries[0:len_list // 2 + 1]
    list2 = countries[len_list // 2 + 1:]

print(len(list1), len(list2))

list3 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
cn, ru, us, *scandic = list3
print(cn, ru, us, scandic)
