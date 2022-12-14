print("Welcome to the Shop!\n")
fruits = {'apple':35,'banana':18,'orange':26}
print("Currently in stock: apple (35p) - banana (18p) - orange (26p) ")
print("Pick an Item, or Enter to Checkout.")
total = 0
basket = ''
while True:
    fr = input("Chioce --> ")
    fr = fr.lower()
    if fr in list(fruits.keys()):
        print("Item added.")
        if total == 0:
            basket += fr
        elif total != 0:
            basket += "-"+fr
        total += fruits[fr]
    elif not fr:
        break
    else:
        print("no such iteam. Try again")
print(f"Thank you. You have purchased {basket} at a cost of {total}p")
