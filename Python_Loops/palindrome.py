""" A palindrome number is a number that remains the same when its digits are 
reversed. In simpler terms,it reads the same forwards and backward. 
For example 121, 5005.
"""

p = int(input("ENTER A NUMBER : "))

p = str(p)
r = p[::-1]
if p == r:
    print(f"{p} is a palindrome number")
else:
    print(f"{p} is not a palindrome number")