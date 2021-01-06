# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 12:21:41 2020

@author: babut
"""

def remove_char(string):
    string = list(string)
    string.remove('o')
    return ''.join(string)


print(remove_char('hello'))




