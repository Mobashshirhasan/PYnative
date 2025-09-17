print("Multiplication Tables from 1 to 10:")
print()

for i in range(1, 21):
    print(f"Table of {i}:")
    for j in range(1, 11):
        result = i * j
        print(f" {j} * {i} = {result}")
    print()