menu = [
    {"item" : "Hotdog", "price": 5.00, "id" : 1},
    {"item" : "Pizza", "price" : 4.00, "id" : 2},
    {"item" : "Candy", "price" : 2.00 , "id" : 3},
    {"item" : "Fries", "price" : 2.00, "id" : 4},
    {"item" : "Meat Pie", "price" : 6.00, "id" : 5}
]

for i in menu:
    print(f"{i['item']} {i['price']} {i['id']}" )

k = input("What would you like?, type the number matching the item")

s = None

for g in menu:
    if g['id'] == k:
      s = g
    break

if s:
    print(f"You chose {s['item']}")

    







      




