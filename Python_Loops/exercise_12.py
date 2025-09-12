"""Write a Python code to check if the given number is a palindrome. 
A palindrome number reads the same forwards and backward. For example, 545 is a palindrome number."""

P = str(input("Enter a number: "))
R = P[::-1]
if P ==R:
    print(f"{P} is a palindrome number")
else:
    print(f"{P} is not a palindrome number")