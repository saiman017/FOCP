# taking a input from user
number = input("Enter a number: ")
# string to integer
number = int(number)
# display the number input by user
print("The numbered entered was", number)
# check the number if it is divisble by 2 
if (number % 2) == 0:
	print("That is an even number")
else:
	print("That is an odd number")