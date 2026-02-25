scan = input("Please input your string to clean: ")
while len(scan) < 1:
    print("Your input string is too short! Try again: ")
    scan = input("Please input your string to clean: ")

clean = ""

for x in scan:
    if x.isalpha() or x.isspace():
        clean = clean + x
    else:
        clean = clean + " "

print(clean)
