
def calculator(option, num1, num2):
	if option == 1:
		return num1 + num2
	elif option == 2:
		return num1 - num2
	elif option == 3:
		return num1 * num2
	elif option == 4:
		return num1 / num2
	


print("""-----select options for calculation-----
	1. For addition
	2. For subtraction
	3. For multipy
	4. For Division
	5. Exit""")



while True:
	opt = int(input("Enter option : "))
	if opt == 5:
		print("Exiting......")
		exit()
	a = int(input("Enter any number : "))
	b = int(input("Enter any number : "))

	calc = calculator(opt, a, b)

	print("--------------------------------------")
	print(f"Your answer is: {calc}")
