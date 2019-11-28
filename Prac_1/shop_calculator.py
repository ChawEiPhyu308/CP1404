
num_items = int(input("Number of items:"))
i =1
total = 0
while i <= num_items:
    price_item = float(input("Price of item:"))
    total += price_item
    i+=1

print("Total price for",num_items,"item is ",total)

if total >100:
    total -= total*0.1
print("Your total price is over 100 and you got 10% discount. Total is :",total)