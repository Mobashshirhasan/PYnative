# "Check if a user-entered string contains any digits using a for loop"

# user_message = input("Enter any message : ")

# digit = False
# for i in user_message:
#     if i.isdigit() == True:
#         digit = True
#         break

# if digit == True:
#     print("It contains a digit")
# else:
#     print("it doesn't contain any digit")







"""print the number as well as their index"""

# user_message = "Hellow01"

# for i in range(user_message):
#     if user_message[i].isdigit():
#         print("is digit", user_message[i])
#         print("index : ", user_message[i])


"""swap the number """

# a = 10
# b = 20
# c = a
# a = b
# b = c

# print(f"a is : ", a)    
# print(f" b is ", b)


# user = int(input("Enter any number: "))

# if user > 0:
#     print("This is positive number", user)

# if user == 0:
#     print("this is zero", user)

# if user < 0:
#     print("this is negative", user)



# if user %  2 == 0:
#     print("the number is even", user)

# else:
#     print("this number is odd", user)



# 1 km = 0.62 miles

# conversion_factor = user * 0.62
# print(conversion_factor, " miles")


# f = (user * 9/5) + 32
# print("farenhiet ", f)


# import calendar

# year = 2026
# month = 10\
# \

# out = calendar.month(year, month)
# print(out)



"""******************** Prime Number ********************"""

    # for i in range(1, num+1):
    #     if num % i == 0:
    #         count = count +1
    # if count > 2:
    #     print(num , "number is not prime")
    # else:
    #     print(num , "number is prime")

    # for i in range(2, num):
    #     if num % i == 0:
    #         count = count + 1
    #         break
    # if count == 1:
    #     print(num ,"is not a prime")
    # else:
    #     print(num, "is a prime")



""" Facttorial """

# num = int(input("Enter a Number: "))

# for i in range(1, num+1):
#     f = i * i
#     print(f)



# str = "hello123"

# digit = False
# for i in str:
#     if i.isdigit() == True:
#         digit = True
#         break

# if digit == False:
#     print("String does not contain any number")
# else:
#     print("String contains a number")






# user = 10

# count = 0
# for i in range(2, user):
#     if user % i == 0:
#         count = count +1
#         break

# if count == 1:
#     print("number is not prime")
# else:
#     print("number is prime")


# str = "Jamesbond"

# kammo = len(str)
# print(kammo)
# result = int(kammo / 2)
# print(result)

# # kammo1 = str[0]

# # kammo1 = int(kammo1 + kammo / 2)

# kammo2 = int( str[kammo -1])

# create a calculator:

# M = int(input("Enter Your First Number : "))
# N = int(input("Enter your Second Number : "))

# # Addition
# print("Addition of M and N : ", M + N)

# # substraction
# print("Substraction of M and N :", M - N)

# # multiplication
# print("Multiplication of M and N :", M * N)

# # Division
# print("Division of M and N :", M / N)

# # Modiulus
# print("Modulus of M and N :", M % N)



# a = input("Enter your name : ")
# print("My name is ", a)


# num = int(input("Enter a number: "))

# count = 0
# for i in range(2, num):
#     if num % i == 0:
#         count = count +1
#         break

# if count == 1:
#     print("Number is not a prime")
# else:
#     print("Number is prime")




"""______String Sclicing_______"""

# names = "harry is a good boy"
# print(len(names))

# # print(names[-4:-2])
# print(names.capitalize())


# str1 = "he's a man , and he is an honesgt man, and he is good man "

# print(str1.find("man"))




"""_________if-else statement______________"""

a = int(input("Enter your Age: "))
print("Your Age is :", a)

if a >= 18 :
    print("You are eligible")

else:
    print("You are not eligible")