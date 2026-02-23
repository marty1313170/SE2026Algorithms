total_cost_for_menu = 0
name = " "
# this is them menu asks your name
def main():

    global name
    name = input("What is your name?")
    return

# shows menu 
def menu():

    global total_cost_for_menu

    b = input("What would you like? Options are \n 1) $4 Pizza 2) $4 Burger 3) $5 Sushi  4) $3 Chips 5) $7 Nachos \n Type the name of the foods you want and seperate them by spaces").lower().split()

    if "pizza" in b:
        total_cost_for_menu +=4
    if "burger" in b: 
        total_cost_for_menu +=4  
    if "sushi" in b:
        total_cost_for_menu +=5
    if "nachos" in b:
        total_cost_for_menu +=7
    if "chips" in b:
        total_cost_for_menu +=3
    return  

# this function calculates if cost needs to be discounted, continue off the total thing 
def discount():
    global total_cost_for_menu
    global name
    discount = total_cost_for_menu - total_cost_for_menu / 10

    if total_cost_for_menu >= 10:
        print(discount, name)
    else:
        print("$", total_cost_for_menu, name)

    return 

main()
menu()
discount()

