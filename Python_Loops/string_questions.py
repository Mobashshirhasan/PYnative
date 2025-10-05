"""Check if a user-entered string contains any digits using a for loop"""

str1 = input("Enter a string: ")

contains_digit = False
  
for i in str1:
    if i.isdigit():
        contains_digit = True
        print("The string contains a digit.")
        break
else:
    print("The string does not contain a digit.")