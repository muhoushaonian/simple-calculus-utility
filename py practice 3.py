#!/usr/bin/env python3

'''
    final exam - simple calculus utility

    Goal:
        In[1]:  euqation: 2 * (x ** 3)  # or any other polynomials in
                                        # standard Python literal format
        Out[1]: result ==> 4999.99xx    # a 4-decimal-place 5000.0-ish value

    Bonus No.1:
        try to read the docs, and utilize **matplotlib** to visualize how the
        error is going down during the calculation process

    Bonus No.2:
        not just polynomials, try equations like "sin(cos(x))"

    Bonus No.3:
        performance optimization, both wiki and your own version are accepted

    Bonus No.4:
        share what you've learned with others at your_github_id.github.io

    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    NOTE:
        Readability Counts 可读性很重要
        Simplicity Counts
        Documentation and Comments Counts

    Deadline:
        push your `integral_answersheet.py` file to your GitHub Repo

                  before 2017.12.31 12:00 AM
'''

__author__ = '潘昭烨'


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


class Integral:
    '''
    The Solution Class

        substitute the `pass` statements with your own code,
        you are allowed to define your own functions in order to keep your
        code clean

    Usage:
        In[1]:  Integral("2 * (x ** 3)", 0, 10)()
        Out[1]: 4999.99xx

        In[2]:  result = Integral("2 * (x ** 3)", 0, 10)
        In[3]:  result()
        Out[3]: 4999.99xx
    '''

    def __init__(self, equation, start, end,
                 default_step=1):
        '''
        Initialize the solution class

        Args:
            equation        - `eval()`-able string like
                              "2 * (x ** 3) - 4 * (x ** 0.5)", where `x` is
                              the placeholder
            start           - integral start
            end             - integral end
            default_step    - float

        Return:
            the integral value
        '''
        self._equation = equation
        self._start = start
        self._end = end
        self._default_step = default_step
        # test if equation is valid
        try:
            eval(equation.replace('x', '123'))
        except SyntaxError: # equation not valid
            print("Unsupported expression!")


    def __call__(self, *args, **kwargs):
        '''
        Do the calculation and return the value
        '''
        equation = input("equation: ")
        start = int(input("start: "))
        end = int(input("end: "))
        a = start
        b = end
        for i in range(1, 50):  # range()函数遍历数字序列
            np.random.seed()  # 随机数函数seed
            x = np.random.random(i * 10) * (b - a) + a  # 生成一个随机x值
            y = eval(equation)
            result = (b - a) * np.sum(y) / len(x)  # 蒙特卡洛法计算定积分
            print(result)


# Testing

if __name__ == '__main__': #模块被引入时，此程序块不执行
    equation = input("equation: ")  # get equation from user
    # test run:
    #   integral from 0 to 10 ( equation ) dx
    print("result ==> {0:.4f}".format( Integral(equation, 0, 10)() ))

