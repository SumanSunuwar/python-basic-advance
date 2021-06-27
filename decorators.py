#Closure in pyhton 
# def multiplier(n):
# 	def times(a):
# 		return a * n
# 	return times 

# times4 = multiplier(4) #times #call by reference
# times5 = multiplier(5)	#=> times

# del multiplier
# print(times4(10)) #=> times(10)
# print(times5(100))

# def login(username):
# 	user = username
# 	if user:
# 		print(f"Welcome! {user}")

# def home_page(func): #func = login
# 	func(input("enter username : ")) #func("david") => login("input")
# 	print("this is homepage..!")
	

# home_page(login) #func reference


#decorators

# def decorators_func(func):
# 	def wrapper():
# 		print("this is before function")
# 		print(func)
# 		func()
# 		print("this is after function")

# 	return wrapper


# @decorators_func
# def example():
# 	print("this is an example")

# print(example) #=>wrapper
# example() #wrapper()

# <function decorators_func.<locals>.wrapper at 0x0000014F6263E430>
# this is before function
# <function example at 0x0000014F6263E3A0>
# this is an example
# this is after function

# this is before function
# <function example at 0x00000199E16AE3A0>
# this is an example
# this is after function


#simple example
# def smart_division(div):
# 	def wrapper(dividend, divisor):
# 		if divisor == 0:
# 			return "can not divide by zero"
# 		else:
# 			return div(dividend, divisor)
# 	return wrapper  #smart_division = wrapper as reference


# @smart_division
# def division(dividend, divisor): #> division = wrapper
# 	return dividend / divisor

# print(division(10, 5)) #=> wrapper(10,5)
# print(division(100, 0))

# 2.0
# can not divide by zero
# def admin_required(func):
# 	def wrapper():
# 		#login condition-code
# 		func()
# 	return wrapper


# def product_view():
# 	print("list of product")



# @admin_required
# def sales_report():
# 		print("Sale report")

# @admin_required
# def price_history():
# 	print("price_history")


#learn about lambda, higher order function(map, filter) km