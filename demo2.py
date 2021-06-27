# mainList = []
# duplicateList = []
# evenList = []
# oddList = []

# for i in range(10):
# 	num = int(input("enter a number : "))

# 	if num not in mainList:
# 		if num % 2 == 0:
# 			evenList.append(num)
# 		else:
# 			oddList.append(num)
		
# 	else:
# 		if num not in duplicateList:
# 			duplicateList.append(num)
		


# 	mainList.append(num)

		


# print("mainlist : ",mainList)
# print("evenlist : ",evenList)
# print("oddlist : ",oddList)
# print("duplicateList : ",duplicateList)





#function
#print(),int(),input(),id(),type() <= known functions = built in function

#def func_name():
	#function body
	#further codes and instruction

#function is block of code = collection code 
#we can define our own funtion
# def func_example():
# 	print("this is example")
# 	print("this is another line of func_example")

# func_example()

# def add_two_numbers(num1, num2):
# 	add = num1 + num2 
# 	print("sum of two numbers: ",add)

# add_two_numbers(5, 10)

# def display_name(name): #<=parameters <= variable
# 	print(name+name)


# display_name("shyam") #<=arguments
# display_name("ram")
# display_name("hari")

# def display_profile(name, contact, address):
	# print("your name:",name)
	# print("your contact:",contact)
	# print("your address:",address)


# #required positional argument
# # display_profile("hari","9876653441","kathmandu")

# #keyword arguments

# name = input("Enter name :")
# address = input("enter address :")
# contact = input("enter contact :")
# display_profile(name=name,address=address,contact=contact)

# def add_two_numbers(num1, num2):
# 	return (num1 + num2) #=> memory store


# a = int(input("enter any number: "))
# b = int(input("enter any number: "))

# answer = add_two_numbers #call by reference

# print(answer(a, b))


# def difference(num1, num2):
# 	if num1 > num2:
# 		return num1 - num2
# 	else:
# 		return num2 - num1


# a = int(input("enter a number: "))
# b = int(input("enter a number: "))

# answer = difference(a, b)

# print(f"difference is : {answer}")

# function => add, differece, mult, div
#calculator = >

# def display_profile(name, address, contact="123456789"):
# 	print(f"your name : {name}")
# 	print(f"your address : {address}")
# 	print(f"you contact : {contact}")


# n = "hari"
# a =  "ktm"
# c = "987654321"


# display_profile(n,a,c)




#define a function = calc
# def calculator(choice, num1, num2):
# 	if choice == 1:
# 		return num1 + num2
# 	elif choice == 2:
# 		return  num1 - num2
# 	elif choice ==  3:
# 		return num1 * num2
# 	elif choice == 4:
# 		return num1 / num2

# #user input 
# print("""--------choices for calculation----------
# 	1 for addtion
# 	2 for subtraction
# 	3 for multiplication
# 	4 for division""")
# choice = int(input("Enter your choice : "))
# print("choice is ",choice)
# a = int(input("enter any number : "))
# b = int(input("enter any number : "))

# result = calculator(choice, a, b)
# print("-----printing your result------")
# print("your answer is: {}".format(result))

# #function call = > execute => output


#list tuple for loop / while function(building own function)

# set , dictionery => data structures
#set => sets unordered, unindexed 





# a = [1, 2, 4, {"one":[5,6, {"two":{"address": "Kathmandu"}}]}]


# school_data = {"student": 
# 		[
# 			{
# 			"id":1,
# 			"name" : "Hari", 
# 			"parents":
# 					[
# 						{"relation": "father", "name": "Ram"}, 
# 						{"relation": "mother", "name": "Sita"},
# 					],
# 			},
# 		]
# 	}

# print("name of mother",school_data.get('student')[0].get('parents')[1].get('name'))







# school_data = {"student": 
# 		[
# 			{
# 			"id":1,
# 			"name" : "Hari", 
# 			"parents":
# 					[
# 						{"relation": "father", "name": "Ram"}, 
# 						{"relation": "mother", "name": "Sita"},
# 					],
# 			},
# 			{
# 			"id":2,
# 			"name" : "Shyam", 
# 			"parents":
# 					[
# 						{"relation": "father", "name": "Ganesh"}, 
# 						{"relation": "mother", "name": "Mina"},
# 					],
# 			},
# 		],

# 		"teacher":[
# 		{
# 		'id':101,
# 		'name':'MR. GB',
# 		'subject': 'science',
# 		},
# 		{
# 		'id':102,
# 		'name':'MR. PK',
# 		'subject': "maths",
# 		},
# 		]
# 	}


# teacher1_id = school_data.get('teacher')[0].get('id')
# teacher1_name = school_data.get('teacher')[0].get('name')
# teacher1_subject = school_data.get('teacher')[0].get('subject')

# teacher2_id = school_data.get('teacher')[1].get('id')
# teacher2_name = school_data.get('teacher')[1].get('name')
# teacher2_subject = school_data.get('teacher')[1].get('subject')


# print(f"teacherID : {teacher1_id}	Name : {teacher1_name}	Subject : {teacher1_subject}")

# print(f"teacherID : {teacher2_id}	Name : {teacher2_name}	Subject : {teacher2_subject}")





# #for loop

# days = ['sunday', 'tuesday', 'thursday']



