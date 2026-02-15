total_cost = 0
name = " "

def main():

    global name
    name = input("What is your name?")
    return

def menu():

    global total_cost

    b = input("What would you like? Options are \n 1) $4 Pizza 2) $4 Burger 3) $5 Sushi  4) $3 Chips 5) $7 Nachos \n Type the name of the foods you want and seperate them by spaces").lower().split()

    if "pizza" in b:
        total_cost +=4
    if "burger" in b: 
        total_cost +=4
    if "sushi" in b:
        total_cost +=5
    if "nachos" in b:
        total_cost +=7
    if "chips" in b:
        total_cost +=3
    return  

def discount():
    global total_cost
    global name
    discount = total_cost - total_cost / 10

    if total_cost >= 10:
        print(discount, name)
    else:
        print("$", total_cost, name)

    return 

main()
menu()
discount()

