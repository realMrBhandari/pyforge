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
    # * V1 logic of fetch function where while loop will fetch each item one by one based on index of category and print them on screen, n starts from 0 and incremets in each iteration and loop works till n < length of category, I like this way as I am in full control here, no absreaction just pure mental model
    # n = 0
    # while n < len(category):
    #  print(f"{n}. {category[n]}")
    #  n += 1

    # * V2 logic of fetch function where for loop will loop over each category without needing to loop over index, this optimized fetch function by eliminating need of looping through indexs and then printing, but counter is still in my hands and I am controling the counter which starts from n = 1 and with each loop it increments, this counter does not effect for loop as now loop is sequence driven rather then counter based like in V1, so n here is for serial numbering for better readability
    # n = 1
    # for each_item in category:
    # print(f"{n}. {each_item}")

    # n += 1
    # * V3 logic of fetch function, it is purely sequence driven and the counter is handeled by loop itself using enumerate, making function perform batter and eliminating unwanted bugs
    for s_no, product in enumerate(category, start=1):
        print(f"{s_no}. {product}")


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
