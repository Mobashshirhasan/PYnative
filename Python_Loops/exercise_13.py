"""Given two lists of numbers, write Python code to create a new list containing odd numbers from the first list and 
even numbers from the second list.

Given:

list1 = [10, 20, 25, 30, 35]   # 25, 35 are odd numbers
list2 = [40, 45, 60, 75, 90]   # 40, 60, 90 are even numbers

"""
new = []
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

# Add odd numbers from list1
for n in list1:
    if n % 2 != 0:
        new.append(n)

# Add even numbers from list2
for n in list2:
    if n % 2 == 0:
        new.append(n)

print("Final List:", new)