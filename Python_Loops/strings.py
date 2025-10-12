# b = "Hello, World!"  #[0,1,2,3,4,5,6,7,8,9,10,11,12,13]
# print(len(b))
# # print(b[:: -1])
# # print(b[::-5])
# print(b[::-2])





""" Shift all the zeros to the right of the list"""
# arr = [1, 2, 0, 3, 0, 4, 5]

# l = len(arr)
# print(l)

# for num in arr:
#     # print(f"element :", num)
#     if num == 0:
#         arr.remove(num)
#         arr.append(num)
# print(arr)






""" Duplicate Array """
arr = [1, 2, 2, 3, 40, 40, 58, 69, 69, 100, 102, 102]

print([len(arr)])
new_arr = []

for num in range(len(arr)-1):
    # print(arr[num])
    if arr[num] != arr[num + 1]:
        new_arr.append(arr[num])

new_arr.append(arr[len(arr)-1])
print(new_arr)
# print(arr[len(arr)-1])


# print(len(arr))
# new_arr = []
# for num in range(len(arr) -1):
#     if arr[num] != arr[num + 1]:
#         new_arr.append(arr[num])

# new_arr.append(arr[len(arr) -1])
# print(arr(len[arr]-1))