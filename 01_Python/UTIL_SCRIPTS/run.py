food_items = [
    ['apple', 'fruit'],
    ['broccoli', 'vegetable'],
    ['banana', 'fruit'],
    ['carrot', 'vegetable'],
    ['cake', 'dessert'],
    ['chicken', 'meat']
]

fruits = [item[0] for item in food_items if item[1] == 'fruit']
veg = [item[0] for item in food_items if item[1] == 'vegetable']

health_tip = f"Eat more {', '.join(fruits[:-1])} and {fruits[-1]} for better health!"

health_tip2 = f"Eat more {', '.join(fruits[:])} and {veg[-1]} for better health!"

print(health_tip)
print(health_tip2)
# (A) Eat more apple, banana and carrot for better health!
# (B) Eat more apple and banana for better health!
# (C) Eat more broccoli, carrot and chicken for better health!
# (D) Eat more apple, banana and broccoli for better health!


print(fruits)
print(fruits[:-1])