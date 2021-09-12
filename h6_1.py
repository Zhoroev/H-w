# 1
names = ['aLfred', 'djonataN', 'irOn MAN', 'vasYa']


def func1(lst):
    return list(map(lambda x: x.upper(), lst))


print(func1(names))

# 2
numbers = [4, 17, 3, 90, 28, 55]


def func2(lst):
    return list(filter(lambda x: x % 2 != 0, lst))


print(func2(numbers))

# 3
from functools import reduce


def func3(lst):
    return reduce(lambda x, y: x * y, lst) * 15


print(func3(numbers))

# 4
palindromes = ['hello', 'sentences where punctuation',
               45, 'Able was I, ere I saw Elba', 34.0, 78.87,
               'found', 'level', '12/11/21', 'radar', 'stats']


def func4(lst):
    all_palindromes = list(
        filter(lambda x: str(x).replace(',', '').lower() == str(x).replace(',', '')[::-1].lower(), lst))
    return reduce(lambda x, y: str(x).replace(',', '').replace(' ', '') + str(y), all_palindromes)


print(func4(palindromes))
