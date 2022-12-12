# -*- coding: utf-8 -*-
"""Assignment_02

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hZv1xb0YMJB6jsO1OW0o8VY_2V2CSS9O

## 1. What are the two values of the Boolean data type? How do you write them?
"""

Two values of Boolean data type: true and false

It is written as False and true respectively.

"""## 2. What are the three different types of Boolean operators?"""

Three different types of Boolean operators:  and , or , and not

"""## 3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate )."""

True and True is True.

True and False is False.

False and True is False.

False and False is False.

True or True is True.

True or False is True.

False or True is True.

False or False is False.

not True is False.

not False is True.

"""## 4. What are the values of the following expressions?

(5 > 4) and (3 == 5)

not (5 > 4)

(5 > 4) or (3 == 5)

not ((5 > 4) or (3 == 5))

(True and True) and (True == False)

(not False) or (not True)
"""

(5 > 4) and (3 == 5)

not (5 > 4)

(5 > 4) or (3 == 5)

not ((5 > 4) or (3 == 5))

(True and True) and (True == False)

(not False) or (not True)

"""## 5. What are the six comparison operators?"""

!=, <=, ==, >, <, and >=

"""## 6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one."""

== is the equal to operator that compares two values and evaluates to a Boolean, while = is the assignment operator that stores a value in a variable.
A condition is an expression used in a flow control statement that evaluates to a Boolean value

"""## 7. Identify the three blocks in this code:
spam = 0

if spam == 10:

print('eggs')

if spam > 5:

print('bacon')

else:

print('hum')

print('spam')

print('spam')
"""

print('eggs')
if spam > 5:
  print('bacon')
else:
  print('hum')
  print('spam')

"""## 8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam."""

print('What is your style? 1 - Middle, 2 - Redneck, other - non')
spam = input()
if spam == '1':
	print('Hello')
elif spam == '2':
	print('Howdy')
else:
	print('Greetings')
