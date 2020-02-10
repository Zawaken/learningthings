#!/bin/env python3
""" Modules """
import os


def fizzbuzz():
    """ fizzbuzz """
    count = 1
    while count <= 100:
        if count % 3 == 0:
            if count % 5 == 0:
                print('FizzBuzz')
                count += 1
            else:
                print('Fizz')
                count += 1
        elif count % 5 == 0:
            print('Buzz')
            count += 1
        else:
            print(count)
            count += 1


def printf():
    """ Print formatting """
    formatting = '{2} {1} {0}'

    print(formatting.format('supported', 'is not', os.name))

    result = 100/777
    print('The result was {:1.3f}'.format(result))

    name = 'Robin'
    age = '22'
    print(f'{name} is {age} years old.')


def lists():
    """ Lists """
    liste = ['one', 'two', 'three']
    listeto = ['four', 'five']
    newlist = liste + listeto
    newlist[0] = 'ONE'
    newlist.append('six')
    newlist.pop()
    print(newlist)
    newlisttwo = ['a', 'e', 'x', 'b', 'c']
    numlist = [4, 1, 8, 3]
    print(newlisttwo)
    print(numlist)
    newlisttwo.sort()
    numlist.sort()
    print(newlisttwo)
    print(numlist)


def dictionaries():
    """ Dictionaries """
    my_dict = {'key1': 'value', 'key2': 'value2'}
    print(my_dict['key1'])
    prices = {'apples': 2.99, 'oranges': 1.99, 'milk': 3.80}
    print(prices['milk'])
    diction = {'k1': 123, 'k2': [0, 1, 2], 'k3': {'insideKey': 100}}
    print(diction['k3']['insideKey'])


def tuples():
    """ Tuples """
    tup = (1, 2, 3)
    print(tup[1])
    tup1 = ('a', 'a', 'b')
    tup1.count('1')
    tup1.index('a')


def setters():
    """ Sets """
    myset = set()
    myset.add(1)
    myset.add(2)
    mylist = [1, 1, 1, 1, 2, 2, 2, 3]
    mississippi = set('mississippi')
    print(myset)
    print(set(mylist))
    print(mississippi)


def booleans():
    """ Booleans """
    print(1 > 2)
    print(1 < 2)
    bat = None
    print(bat)


def iobasicfiles():
    """ i/o with basic files in python """
    myfile = open('myfile.txt')
    contents = myfile.read()
    print(contents)
    myfile2 = open("/home/zawaken/olkborderqueue")
    print(myfile2.read())
    myfile.close()
    myfile2.close()
    with open('myfile.txt') as my_new_file:
        contents = my_new_file.read()
        print(contents)
    with open('mynewfile.txt', mode='r') as fix:
        print(fix.read())
    with open('mynewfile.txt', mode='a') as fix:
        fix.write('\nFour on fourth')
    with open('testinyes.txt', mode='w') as fix:
        fix.write('I Created this file with Python!')
    with open('testinyes.txt', mode='r') as fix:
        print(fix.read())


fizzbuzz()
