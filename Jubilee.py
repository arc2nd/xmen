#!/usr/bin/python

from Xman import *

class Jubilee(Xman):
    def __init__(self, universe):
        super(Jubilee, self).__init__(fname='Jubilation', lname='Lee', sname='Jubilee')
        self.power_list = ['independence day', 'energy blast', 'photo flash']

    def run(self, direction='backward'):
        print('{} runs backwards'.format(self.sname))
        return

    def hide(self, where='in the bushes'):
        print('{} hides in the bushes'.format(self.sname))
        return

    def fight(self, how='energy blast'):
        power_string = ', '.join(self.power_list)
        print('How do you want to fight?\nChoose: {}'.format(power_string))
        choice = raw_input('> ')
        if 'day' in choice.lower():
            self._independence_day()
        elif 'blast' in choice.lower():
            self._energy_blast()
        elif 'flash' in choice.lower():
            self._photo_flash()
        else:
            print('Too slow, you dead.')
        return

    def panic(self, how='freeze'):
        print('{} freezes when she panics'.format(self.sname))
        return

    def _independence_day(self):
        print('{} uses independence day, it\'s very effective'.format(self.sname))
    
    def _energy_blast(self):
        print('{} uses energy blast, meh'.format(self.sname))

    def _photo_flash(self):
        print('{} uses photo flash, it\'s not very effective'.format(self.sname)) 
