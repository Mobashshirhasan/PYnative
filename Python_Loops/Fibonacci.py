"""Generate Fibonacci series up to 15 terms """


# num1 = 0
# num2 = 1

# print("Fibonacci series:")
# for num in range(10):
#     print(num1)
#     result = num1 + num2
#     num1 = num2
#     num2 = result
    



num1 = 0
num2 = 1
dig = 8
print("Fabonnaci Series. ")
print(num1)
print(num2)

for num in range(2, dig):
    # print(num1)

    temp = num1 + num2
    print(temp)

    num1 = num2
    num2 = temp
# print(num2)