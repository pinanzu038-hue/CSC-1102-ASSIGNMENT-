print("Welcome to CATUC POS")
num_items = int(input("How many items were purchased? "))
items_cost = []
items_name = []
items_quantity = []
items_unit_price = []


for item in range (1, num_items +1):
    name = str(input(f"Enter the name of item {item}: "))
    cost = float(input(f"Enter the cost(unit price) of N{name}: "))
    quantity = float(input(f"How many {name} did you buy? "))
    total_price = cost * quantity
    items_unit_price.append(cost)
    items_name.append(name)
    items_quantity.append(quantity)
    items_cost.append(total_price)
    
items_cost_total = sum(items_cost)
if items_cost_total > 10000:
    discount = items_cost_total * 0.3
    total_cost = items_cost_total - discount
elif (len(items_cost) > 5) and (items_cost_total > 4000):
    discount = items_cost_total * 0.15
    total_cost = items_cost_total - discount
elif items_cost_total > 5000:
    discount = items_cost_total * 0.1
    total_cost = items_cost_total - discount
else:
    total_cost = items_cost_total

print("--- RECEIPT ---")
print(f"{'S/N':<6} | {'Description':<15} | {'Quantity':<12} | {'Unit Price':<14} | {'Total Price':<10}")

for i in range(num_items):
    print(f"{i+1:<6} | {items_name[i]:<15} | {items_quantity[i]:<12} | {items_unit_price[i]:<14} | {items_cost[i]:<10}\n")

print(f"Total - {items_cost_total}")
print(f"Discount - {discount}")
print(f"Total Price to Pay - {total_cost}")
print("Thanks for your patronage")
    
    
