"""Write a Python code to display numbers from a list divisible by 5."""

number = [10, 20, 33, 46, 55]

for num in number:
    if num % 5 ==0:
        print("Number divisible by 5 is: ", num)
    else:
        print("Number not divisible by 5 is: ", num)