"""Generate Fibonacci series up to 15 terms """


num1 = 0
num2 = 1

print("Fibonacci series:")
for num in range(10):
    print(num1)
    result = num1 + num2
    num1 = num2
    num2 = result
    