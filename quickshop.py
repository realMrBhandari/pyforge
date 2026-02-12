# programme for simulating a self checkout kiosk in a mid-sized grocery store
total = None
delivery = None
inventory_fruits = [
    "banana",
    "apple",
    "orange",
    "pomegranate",
    "papaya",
    "guava",
    "coconut",
    "pineapple",
    "watermelon",
    "muskmelon",
    "grapes",
]
inventory_vegetables = [
    "potato",
    "onion",
    "tomato",
    "carrot",
    "cabbage",
    "cauliflower",
    "mashroom",
    "lettuce",
    "cucumber",
    "capsicum",
    "garlic",
    "beetroot",
    "sweet potato",
]
inventory_dairy = [
    "milk",
    "chedder cheese",
    "mozzarella cheese",
    "curd",
    "yogurt",
    "cream",
]
inventory_bakery = ["Bread", "Buns", "Cake", "Doughnuts"]
inventory_beverages = ["Water", "Ice Tea", "Coffee", "MoguMogu"]
inventory_households = ["Colin", "Vim", "Soap", "Tissue"]


# ?
def products_fetch(category):
    n = 0
    while n < len(category):
        print(f"{n}. {category[n]}")
        n += 1


print(
    """\033[38;5;214m============================================================
||                   QUICK SHOP CHECKOUT                  ||
============================================================\033[0m"""
)
print(
    "======== Please select a product category ======== \v"
    "1. Fruits  \v"
    "2. Vegetables\v"
    "3. Dairy\v"
    "4. Bakerey\v"
    "5. Beverages\v"
    "6. Household Essentials\v"
)
category_choice = input("Enter choice (\033[35m1\033[om - \033[35m6\033[0m)")
