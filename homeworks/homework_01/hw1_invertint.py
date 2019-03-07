#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''
    if str(number).isdigit():
        if (number != 0):
            return int(str(number).rstrip("0")[::-1])
        else:
            return 0
