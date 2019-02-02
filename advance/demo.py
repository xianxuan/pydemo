#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:])
print(L[:-1])  # 左闭右开
print(L[-1:])
L = list(range(100))
# 每两个取一个
print(L[:10:2])
# 所有数每五个取一个
print(L[::5])
# 甚至什么都不写，只写[:]就可以原样复制一个list
C = L[:]
print(C)
# string和tuple也可以进行切片操作但是tuple不可变
Q = (0, 1, 2, 3, 4, 5)
print(Q)
Q = Q[:-1]
print(Q)
# strip() 方法用于移除字符串头尾指定的字符（默认为空格)
ss = "*****this is string example....wow!!!*****"
print(ss.strip('*'))

# 迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
for value in d.values():
    print(value)
for k, v in d.items():
    print(k, v)
# 当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行
from collections import Iterable

isinstance('abc', Iterable)  # True
isinstance([1, 2, 3], Iterable)  # True
isinstance(123, Iterable)  # False
# enumerate函数可以把一个list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

# 列表生成式
print(list(range(1, 11)))
print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])
import os

print([d for d in os.listdir('.')])
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

# 生成器
g = (x * x for x in range(10))
# yeild的函数就是一个生成器，记录执行位置，用到时在执行


# 迭代器
# 可以直接作用于for循环的对象统称为可迭代对象：Iterable
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator(生成器就都是迭代器)
from collections import Iterator

isinstance((x for x in range(10)), Iterator)  # True
isinstance([], Iterator)  # False
isinstance({}, Iterator)  # False
isinstance('abc', Iterator)  # False
# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator
# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator
isinstance(iter([]), Iterator)  # True

# 高阶函数
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
print(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# lambda定义简单的匿名函数
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(str2int("1345"))


# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))


# Iterator惰性计算可以看作放到了list中需要的时候再拿出来
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5


d = odd()
print(next(d))
print(next(d))
print(next(d))

# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
print(sorted([36, 5, -12, 9, -21], key=abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))


# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()


# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
def count():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。

# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果


# 装饰器
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log('execute')
def now():
    print('2015-3-25')


now()

# 偏函数
# 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
import functools

# 创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
int2 = functools.partial(int, base=2)  # **kw
max2 = functools.partial(max, 10)  # *args

# 每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。__init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mycompany


import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


# 当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试

# 类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名
# _xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用(如果你非要那也没办法)

# 获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法
import pickle

d = dict(name='Bob', age=20, score=88)
# pickle.dumps(d)
f = open('dump.txt', 'w')
# pickle.dump(d, f)
import json

json.dump(d, f)
while True:
    pass
