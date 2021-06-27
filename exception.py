#exception handling
try:
	num1 = int(input("enter a number: "))
	num2 = int(input("enter another number: "))

except ValueError as err:
	print("characters cannot be integer")

else:
	print("sum of numbers: ",num1 + num2)


print("this is rest of the code")










structure of exception handling (try/except)
# try:
# 	pass
# except Exception as err:
# 	pass
# except Exception as err:
# 	pass
# else:
# 	pass
# finally: => #resources closing => library(selenium)=>open=close
