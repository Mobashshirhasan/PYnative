"""Calculate the sum of even numbers upto a given number n."""

"""
🧠 Think of it like this:

Imagine you're keeping a piggy bank, and you add ₹2, ₹4, ₹6... every time you find an even number.

Here’s what happens behind the scenes:

Let's say n = 6

| `i` | Is Even? | `sum_even` |
| --- | -------- | ---------- |
| 1   | ❌ No     | 0          |
| 2   | ✅ Yes    | 0 + 2 = 2  |
| 3   | ❌ No     | 2          |
| 4   | ✅ Yes    | 2 + 4 = 6  |
| 5   | ❌ No     | 6          |
| 6   | ✅ Yes    | 6 + 6 = 12 |
"""

n = int(input("Enter a number: "))
sum_even = 0

for i in range(1 , n+1):
    if i % 2 ==0:
        sum_even += i

print(f"The sum of even numbers upto {n} is: ", sum_even)
