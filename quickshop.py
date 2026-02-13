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
    """======== Please select a product category ========
1. Fruits  
2. Vegetables
3. Dairy
4. Bakerey
5. Beverages
6. Household Essentials\v"""
)
category_choice = input("Enter choice (\033[35m1\033[0m - \033[35m6\033[0m): ")
category_choice_validation = ["1", "2", "3", "4", "5", "6"]
while category_choice not in category_choice_validation:
    category_choice = input(
        "\033[31mIncorrect Input! Try again\033[0m (\033[35m1\033[0m - \033[35m6\033[0m):"
    )

match category_choice:
    case "1":
        products_fetch(inventory_fruits)
    case "2":
        products_fetch(inventory_vegetables)
    case "3":
        products_fetch(inventory_dairy)
    case "4":
        products_fetch(inventory_bakery)
    case "5":
        products_fetch(inventory_beverages)
    case "6":
        products_fetch(inventory_households)
