# -*- coding: utf-8 -*-
"""
人类类

Created on Fri Jan 10 16:02:14 2020

@author: fenggr
"""

class Human():
    """
    人类
    """
    
    def __init__(self):
        self.__age__ = 0

    def addAge(self):
        self.__age__ += 1
    
    def __Age__(self):
        return self.__age__
    
    age = property(__Age__)
    

class Man(Human):
    """
    男人
    """
    
    def __init__(self):
        super().__init__()
    

class Woman(Human):
    
    def __init__(self):
        super().__init__()
        self.__hy__=False
        
    def __get_hy__(self):
        return self.__hy__
    
    def set_hy(self):
        '''
        设置怀孕状态，True为怀孕
        '''
        self.__hy__ = True
        
    hy = property(__get_hy__)
    
    
