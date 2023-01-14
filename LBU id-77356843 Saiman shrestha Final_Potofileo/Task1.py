import random
#Creating three list for genrating 512 password combination.
Const = ['hem','mohan','sushan','birajan','suyog','naitik','sushil','raj']
colour = ['red','yellow','blue','orange','pink','black','purple','green']
fruit = ['apple','banana','grape','orange','watermelon','kiwi','lichi','blueberry']

#Creating list having 512 different password
list_combination = [(i+j+k) for i in Const for j in colour for k in fruit]
print("""Password Generator
==================\n""")
#infinite loop
while True:
    try:
        #Taking input from user to display needed password.
        user_input = int(input("How many passwords are needed?:"))
        if (user_input < 1) or (user_input > 24):
            print("Please enter a value between 1 and 24.")
        else:
            # electing inputed numbers of random password from above list.
            generated_pass = random.choices(list_combination, k=user_input)
            break
    #if the input value is string print below condition.
    except ValueError:
        print("Please enter a number.")
#printing number from 1 to 24 in list
num_list = [i for i in range(1,25)]
#combining two list into tuples in list.
n = list(zip(num_list, generated_pass))
#Display password
for i, j in n:
    print(f"{i} --> {j}")