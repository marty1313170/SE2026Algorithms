total_cost = 0

a = input("What is your name?")

b = input("Our menu: \n Pizza $3.00 \n Burger $4.00 \n Chips $2.00 \n Soda $2.00 \n Nuggets $5.00 \n What you you like? \nif there are mulitple items seperate them by spaces").lower().split()

if "pizza" in b:
    total_cost +=3
if "burger" in b:
    total_cost +=4
if "chips" in b:
    total_cost +=2
if "soda" in b:
    total_cost +=2
if "nuggets" in b:
    total_cost +=5

discount = total_cost - total_cost / 10 

if total_cost >= 10:
    print(discount, a)
else:
    print("$", total_cost, a)

