#lambda + higher order functions(map & filter)

# def func_name(x):
# 	return x + 1

# func_name(5)

# function without name => anonymous func
# called where defined => no need to define at one place and call in one place

#stucture of lambda

# lambda <variables or params>:<body>
# lambda param1, param2, param3,.......:return
# lambda x: x + 1
#keyword => lambda , variable => x, body=> x+1

# divide_by_5 = (lambda x: x / 5)

# add = lambda x, y: x + y 

# print(add(4,6))
#once used by defining or creating once
# lambda first_name, last_name:
# f'Fullname : {first_name.capitalize()} {last_name.title()}'
# print(fullnaming("david", "beckhams"))

#higher order functions

# alist = [1,2,3,4,5]

# for num in alist:
# 	#elements manipulates/ changes
# 	print(i+1)

#map => optimal use => fast result => production or exe => fast

# map(mapping_function, *iterables) => mapped obj

# alist = [1, 2, 3, 4, 5 ,6 ,7]
#req ans = [3, 4, 5, 6, 7, 8, 9]

# def increase_by_two(val):
# 	return val + 2

# #keyword=>map(func,iterable_object)

# ans = list(map(increase_by_two, alist))
# print(ans)
# #[3, 4, 5, 6, 7, 8, 9]

# alist = [1, 2, 3, 4, 5 ,6 ,7]

# ans = list(map(lambda val:val + 2, alist))

# print(ans)
# [3, 4, 5, 6, 7, 8, 9]

# flow => declaring a list => map obj => type casting into list

# namelist = ["ram", "sita", "hari", "binod"]

# # uppernames = [list of first letter be capital]

# uppernames = list(map(lambda name:name.title(),namelist))
# print(uppernames)

# email_list = ["abc@gmail.com", "xyz@yahoo.com", "test@hotmail.com"]

# # ans = ["gmail.com", "yahoo.com", "hotmail.com"]

# ans = list(map(lambda email:email.split("@")[1], email_list))
# print(ans)

# # ['gmail.com', 'yahoo.com', 'hotmail.com']


#filter
#map returns changed obj
#filtering => true and false

# filter(filter_func, iterable_object)

# alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ans = list(filter(lambda num:num % 2 == 0,alist))
# print(ans)

#[2, 4, 6, 8, 10]

#[2, 4, 6, 8, 10]

# email_list = ["abc@gmail.com","ram@gmail.com", "xyz@yahoo.com","demo@gmail.com", "test@hotmail.com"]

# # gmail_list = [<gmail.com>]

# ans = list(filter(lambda email: email.endswith("@gmail.com"), email_list))
# print(ans)

