# print("Multiplication Tables from 1 to 10:")
# print()

# for i in range(1, 21):
#     print(f"Table of {i}:")
#     for j in range(1, 11):
#         result = i * j
#         print(f" {j} * {i} = {result}")
#     print()


def exponent(base, exp):
    result = 1  # Initialize result to 1 for multiplication
    
    # Handle special case: any number^0 = 1
    if exp == 0:
        return 1
    
    # Multiply base by itself exp times
    for i in range(exp):
        result *= base
    
    return result

# Test cases as per your requirements
print("Case 1:")
base1 = 2
exponent1 = 5
result1 = exponent(base1, exponent1)
print(f"{base1} raises to the power of {exponent1}: {result1}")
print(f"i.e. ({' *'.join([str(base1)] * exponent1)} = {result1})")