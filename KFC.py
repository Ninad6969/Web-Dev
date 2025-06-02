# Welcome message
print("Welcome to KFC Dhaka")

# Menu dictionary
Menu = {
    "Chicken Fried": 299,
    "Frech Fries": 149,  
    "Chicken Popcorn": 139,
    "Binger Burger": 349,  
    "Softy": 29,
    "Cold Coffee": 79
}


print("Available Menu")


for item, price in Menu.items():
    print(f"{item} : {price} Rupees")


order = input("Enter Your Order (Select Only One Item): ")


if order in Menu:
   
    print(f"{order} Available! Please Proceed with the Payment")
    price = Menu.get(order) 
    
    total_bill = price + 21.90
    print(f"Your Total Bill {price} + 21.90 Rupees Tax")
    print(f"{total_bill} Rupees")
    
    payment = input("Press Enter to Make Payment") 
    
    print("Payment Successfull Please Collect Your Order")
else:
   
    print(f"{order} not Available")
