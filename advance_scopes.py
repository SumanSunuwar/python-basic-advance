#scopes = > global and local scope

# num = 10 # gloabal variable (Immutable obj)

# def some_func():
# 	global num
# 	num += 1 #local variable
# 	print(f"this is inside function: {num}")


# print(f"value of num before function exec: {num}")
# some_func()
# print(f"value of num after function exec: {num}")


# alist = [1,2,3,4] #global (immutable)

# def func():
# 	alist.append(10)
# 	print(f"inside function: {alist}")

# print(alist)
# func()
# print(alist)

# def outer_function():
# 	def inner_func():
# 		print("this is inner function")


# 	inner_func()
# 	print("this is outer function")

# outer_function()



# def main():
# 	num = 10
# 	def inner_func():
# 		nonlocal num
# 		num = num + 5
# 		print(num)
# 	inner_func()

# main()

# def outer_function(n):
# 	def first_func():
# 		print("this is first function")
# 	def second_func():
# 		print("this is second function")
# 	if n == 1:
# 		return first_func
# 	if n == 2:
# 		return second_func
# first = outer_function(1) = first_func
# second = outer_function(2) = second_func
# first()
# second()

# def main(n):
# 	def add(a,b):
# 		return a+b
# 	def sub(a,b):
# 		return a-b
# 	if n == 1:
# 		return add
# 	elif n == 2:
# 		return sub

# func_add = main(1) # referencing inner add function = add
# func_sub = main(2) #referencing inner sub function = sub

# print(func_add(12,3))
# print(func_sub(12,3))

#home => login()
#post => login()
#message => login()




# def greet(name):
# 	print(f"Welcome {name}")

# # greet("ram")
# def greet_shyam(func):
# 	func("shyam")

# def greet_ram(func): #func = greet
# 	func("Ram")  #greet("Ram")

# greet_ram(greet) 
# greet_shyam(greet)


