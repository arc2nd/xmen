#!/usr/bin/env python

class Square(object):
    def __init__(self, sqName=None):
        # things to do to make a square
        self.name = sqName
        return
    def action(self):
        # an action that can be performed with a square
        print('my name is: ' + self.name)
        return

class Circle(object):
    def __init__(self, ciName=None):
        return

if __name__ == '__main__':
    sq = Square(sqName='seven')
    sq.action()

