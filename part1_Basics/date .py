# encoding: utf-8

##################################################
# This script shows an example of a header section. This sections is a group of commented lines (lines starting with
# the "#" character) that describes general features of the script such as the type of licence (defined by the
# developer), authors, credits, versions among others
##################################################
#
##################################################
# Author: Yohan Wadia
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Yohan Wadia
# Email: yohanswadia@gmail.com
# Status: development
##################################################

# End of header section

x = 1996
y = 23
z = 'August'
print(y,z,x)


import calendar

date = calendar.weekday(2021,9,27)
dayname = calendar.day_name[date]

print('we have a programming class on',dayname)

