"""Print the following pattern
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
"""

# n = 5  # number of rows

# for i in range(1, n + 1):
#     for j in range(i):
#         print(i, end="  ")
#     print()



for num in range(6):
    for i in range(num):
        print (num, end=" ") # print number
    # new line after each row to display pattern correctly
    print("\n")