Menu={
    "burger":270,
    "pizza":500,
    "coffee":200,
    "salad":40,
}
# greet
print("welcome to Python restuarant")
print("burger=Rs: 270\npizza=Rs: 500\nsalad=Rs: 40\ncoffee=Rs: 60")
# defining variable of order total
order_total=0
# input from customer
customer_order_1=(input("select you want to order: "))
if customer_order_1 in Menu:
    order_total+=Menu[customer_order_1]
    print(f"Your order {customer_order_1} is placed! please wait 15 minutes!")
else:
    print(f"The order {customer_order_1} is not in our Menu!")
# another order

customer_order_2=input("Do you want to order something other in our Menu? (yes/no)") 
if customer_order_2=="yes":
    item_2=input("select in ubove Menu you want to order.")
    if item_2 in Menu:
        order_total+=Menu[item_2]
        print(f"Your order {item_2} has been placed! wait 15 minutes")
    else:
        print(f"Your order {item_2} is not in our Menu!")

print(f"Total amount of items to pay is {order_total}")        

