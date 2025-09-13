"""Get each digit from a number in the reverse order.For example, If the given integer number is 7536, 
the output shall be “6 3 5 7“, with a space separating the digits.

Given:

number = 7536
# Output 6 3 5 7 
"""

number = 7536

result = " ".join(str(number)[::-1])

print(result)