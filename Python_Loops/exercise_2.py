# Write a Python code to print the following number pattern using a loop.

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

"""Hint : Decide on the row count, which is 5, because the pattern contains five rows.
Run the outer loop 5 times using a for loop and the range() function.
Run the inner loop i+1 times using a for loop and the range() function.
In the first iteration of the outer loop, the inner loop will execute one time.
In the second iteration of the outer loop, the inner loop will execute two times.
In the third iteration of the outer loop, the inner loop will execute three times, and so on, until row 5.
Print the value of j in each iteration of the inner loop (j is the inner loop iterator variable).
Display an empty line at the end of each iteration of the outer loop (an empty line after each row).
"""

# Using while loop
# i = 1
# n = 5

# while i <= n:
#     j = 1
#     while j <= i:
#         print(j, end=' ')
#         j += 1
#     print()  # New line after each row
#     i += 1



i = 1
n = 5

while i <= n:
    j = 1 
    while j <= i:
        print(j, end='  ')
        j += 1
    print()  # New line after each row
    i += 1