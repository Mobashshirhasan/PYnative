"""Write Python code to iterate through the first 10 numbers and, in 
    each iteration, print the sum of the current and previous number."""

# previous_num = 0
# n= [1,2,3,4,5]

# for i in range(len(n)):
#     current_item = n[i]
#     if i == 0:
#         previous_num=0
#     else:
#         previous_num= n[i - 1]

#     print(previous_num)



previous_num = 0

for i in range(1, 11):
    Total_sum = previous_num + i
    print("Current number", i , "previous number: ", previous_num , "sum : ", Total_sum)
    previous_num = i
