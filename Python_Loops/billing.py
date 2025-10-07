# Billing 

"""

"""


customer_item = int(input("Enter the no. of Items : "))

list_of_items=[] 

for i in range(customer_item):
    item_price = int(input(f'Enter the price of {i+1} item: '))
    list_of_items.append(item_price)
# print(list_of_items)

total_amount = 0
for i in list_of_items:
    total_amount = total_amount + i 
print("Total Amount : ", total_amount)

if total_amount >= 10000:
    discounted_amount = (total_amount*30)/100
    print("Discounted Amount: ", discounted_amount)

elif total_amount >= 3000:
    discounted_amount = (total_amount*20)/100
    print("Discounted Amount: ", discounted_amount)

elif total_amount >= 2000:
    discounted_amount = (total_amount*10)/100
    print("Discounted Amount: ", discounted_amount)
    
net_amount = total_amount - discounted_amount
print("Net Amount: ",net_amount)