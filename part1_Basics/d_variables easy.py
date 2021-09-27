# encoding: utf-8

##################################################
# This script shows an example of variable assignment. It explores the different options for storing vales into
# variables
##################################################
#
##################################################
# Author: Diego Pajarito
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Diego Pajarito
# Email: diego.pajarito@iaac.net
# Status: development
##################################################

# We don't need any library so far

# Let's write our code

# Let's create two variables and assign them two values

x = 99
y = 63

# Let's assign the result of an operation to a third variable
z = x * y


# Let's print out the result
print('The value assigned is:')
print(z)

# Let's assign the result of an operation to a third variable
z = x * y - x + y

# Let's print out the result
print('The value assigned is:')
print(z)

# Let's assign a new value to this variable and print again
z = x - y
print('The value assigned now is:')
print(z)


# We can also assign values or variable's values
x = z
y = 'Now I store text'

# Let's see how we ended up storing values
print('The value in -x- now is:')
print(x)
print('The value in -y- now is:')
print(y)
print('The value in -x- now is:')
print(z)


