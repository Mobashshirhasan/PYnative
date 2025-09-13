"""Write a Python code to check if the given number is a palindrome. 
A palindrome number reads the same forwards and backward. For example, 545 is a palindrome number."""

P = str(input("Enter a number: "))
R = P[::-1]
if P ==R:
    print(f"{P} is a palindrome number")
else:
    print(f"{P} is not a palindrome number")



""" look at [::-1]:

start → empty → means “start from the end”

end → empty → means “go until the start”

step = -1 → go backwards one character at a time

So Python takes your string from end to start, one by one. """