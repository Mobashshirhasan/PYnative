"""Write Python code to iterate through the first 10 numbers and, in 
    each iteration, print the sum of the current and previous number."""


# previous_num = 0

# for i in range(1, 11):
#     Total_sum = previous_num + i
#     print("Current number", i , "previous number: ", previous_num , "sum : ", Total_sum)
#     previous_num = i

# print table of 2:
# for i in range(1, 11):
#     result = 2 * i
#     print(f" 2 * {i} = {result}")


# Print the table from 1 to 10: 
# for i in range(1, 11):
#     print(f"Table of {i}:")
# for j in range(1, 11):
#     # print(f" {i} * {j} = {i * j}")
#     print(f"{i} × {j} = {i * j}")

# for i in range(1, 11):
#     print(f"Table of {i}:")
#     for j in range(1, 11):
#         print(f"{i} × {j} = {i * j}")

# 7536 reverse this number:
num = 7536

reversed_num = int(str(num)[::-1])
print(reversed_num)  # Output: 6357
