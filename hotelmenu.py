#Menu of Resturant
menu ={
    'Pizza' : 150,
    'Burger' : 60,
    'Chicken chow' : 80,
    'Coffee' : 50,

}
print("Welcome to pheniox Resturant")
print("Pizza: Rs. 150 \n" "Burger : Rs. 60\n" "Chicken chow : 80\n""Coffee : 50")

order_total = 0
item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1}has been added to your order")
else:
    print(f"ordered item {item_1}is not avaialable yet")

another_order = input("Do you want to add another item ? (yes/no)")
if another_order == "yes":
    item2 = input("Enter the name of second item = ")
    if item2 in menu:
        order_total += menu[item2]
        print(f"item {item2} has been added to order")
    else:
        print(f"ordered item {item2} is not avaialable !")
    print(f"The total amount of item to pay is {order_total}")
