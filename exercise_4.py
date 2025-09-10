"""Write a Python code to accept a string from the user and display characters
present at an even index number.For example, str = "PYnative". so your code 
should display ‘P’, ‘n’, ‘t’, ‘v’."""

user_input = input("Enter a String : ")
print(f"Original String is : {user_input}")

count = len(user_input)
print("Printing only even index ")
for i in range(0 , count - 1 , 2):
    print("index [", i ,"]", user_input[i])
