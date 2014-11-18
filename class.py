#!/usr/bin/env python
# -*- coding: utf-8 -*-
import types

class Student():
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def priint_souce(self):
        print '%s:%s' %(self.__name,self.__score)

    def get_grade(self):
        if self.score >=90:
            print  'A'
        elif self.score >=60:
            print  'b'
        else:
            print  'C'

    def get_name(self):
        return  self.__name

    def get_score(self):
          return self.__score

    def set_name(self,name):
        self.__name = name

    def set_score(self,score):
        if 0<=score<=100:
            self.__score = score
        else:
            print ('Bad score')
    def get_dir(self):
        print  dir(self)

if  __name__ =="__main__":
    Tom = Student('zhangzhuoran',16)
    Tom.get_dir()
    if  hasattr(Tom,'get_dir'):
        print 'ok'
    else:
        print 'no'

