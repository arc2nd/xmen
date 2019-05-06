#!/usr/bin/python

# import the Jubilee class
import Jubilee

# instantiate a specific Jubilee from Universe 616
j616 = Jubilee.Jubilee(universe=616)

# run Jubilee-616 through her actions
j616.run()

j616.hide()

j616.fight()

j616.panic()

# check Jubilee-616's given name and Xman callsign
print('Name: {} {}\n AKA: {}'.format(j616.fname, j616.lname, j616.sname))



