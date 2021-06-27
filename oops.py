# class Television:
# 	#initiaization function(object initialize)
# 	def __init__(self,brand,color,resolution):
# 		self.brand = brand
# 		self.color = color
# 		self.resolution = resolution

# 	def power_on(self):
# 		print(f"{self.brand} is starting.")

# 	def running_prgm():
# 		pass


# tv1 = Television('samsung', 'silver','1024') #instance of an object creating

 # __init__() missing 3 required positional arguments: 'brand', 'color', and 'resolution'


#object => everything arround us are object(eg mobile,tv,dog,bike)
#object in programmming
#representaion of these real world objects in programming language
#classes => template/blueprint for real world entities/object
#classes are also user build datatype
#oops = > concept of representing real world objects in programming
#class => template for real world objects




# class Employee:

#     def __init__(self,_id,name,age,salary):
#         #instance variable
#         self._id = _id
#         self.name = name
#         self.age = age
#         self.salary = salary

#         #instance method
#     def employee_details(self):
#         print(f"EmployeeID : {self._id}")
#         print(f"Name : {self.name}")
#         print(f"Age : {self.age}")
#         print(f"Salary : {self.salary}")



# e1 = Employee("001", "Ram", "35", "50000") #instanciating object
# e1.employee_details()

# # EmployeeID : 001
# # Name : Ram
# # Age : 35
# # Salary : 50000


# class Student:
#     #class / static variable
#     college_name = "Xyz intl" 

#     def __init__(self,name,grade,roll_no):
#         #instance variable
#         self.name = name
#         self.grade = grade
#         self.roll_no = roll_no

#         #instance method
#     def study(self):
#         print(f"{self.name} is studying.")

# st1 = Student("david","X", "100")
# st2 = Student("luke", "X", "101")

# print(st1.college_name)
# print(st2.college_name)
# print(st.name)
# print(st1.__dict__)
# print(st2.__dict__)

# p1.name = "diva"

# Xyz intl
# Xyz intl
# {'name': 'david', 'grade': 'X', 'roll_no': '100'}
# {'name': 'luke', 'grade': 'X', 'roll_no': '101'}


#encapsulation, inheritance, polymorphism, abstraction
#access modifiers, accessors(getter func) and mutators(setter func)



#encapsulation = hiding aspects of objects(features / behaviour)
#eg (TV remote = insides hidden)
#enclosing = eg(medicine cover)









# class Product:
#     def __init__(self,name,price):
#         self.name = name
#         #private varaible
#         self._price = price #_Product__price(name mangaling)

#     # #getter concept(accessor)
#     # def get_price(self):
#     #     return self._price

#     # #setter concept(mutator)
#     # def set_price(self,price):
#     #     if price <= 0:
#     #         print("Price cannot be zero or less than zero")
#     #     else:
#     #         self._price = price





# p1 = Product("Tshirt", 500)
# print(p1._price)
# p1._price = 200
# print(p1._price)
# print(p1.__dict__)

# class Student:
#     def __init__(self,name):
#         self._name = name
#     @property
#     def name(self):
#         return self._name
#     @name.setter
#     def name(self,newname):
#         self._name = newname

# std = Student("Swati")
# print(std.name)
# std.name = 'Dipa'
# print(std.name)
# print(std._name) # still accessible


#access modifier =(public members, protected, private)


# class Student:
#     #class variable or attribute
#     school_name = "abc school"

#     def __init__(self,name,age):
#         #instance attributes or variable
#         self.__name = name #protected attribute
#         self.age = age

#     #getter function(accessor)
#     @property
#     def name(self):
#         return self.__name

#     @name.setter
#     def name(self,newName):
#         self.__name = newName

#     #instance method
#     def study(self):
#         print(f"{self.name} is studying")

# st1 = Student("ram","25") #=> instantiate new object
# print(st1.__dict__)
# print("name:",st1.name) #>getter
# st1.name = "shyam"
# print("changed name",st1.name)

#excapsulation = > attributes and members are hidden and not accessible directly
#wrapping of data & methods into class so data and inf. hidden
#python only by convention private not by rule

#@classmethod & staticmethod

#class method can return an object of class
#class method can be called useing ClassName.methodname()
#class method is also called syntatic sugar
# from datetime import date


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def birthYear(cls,name,yob):
#         #return Student("Hari",20)
#         return cls(name,date.today().year - yob)

# st1 = Student("Hari",20)
# print(st1.__dict__) 

# st2 = Student.birthYear("shyam", 1995)
# print(st2.__dict__)

# # {'name': 'Hari', 'age': 20}
# # {'name': 'shyam', 'age': 26}


# class Calculator:
#     def __init__(self,num1,num2):
#         self.num1 = num1
#         self.num2 = num2

#     def add(self):
#         if Calculator.is_even_or_odd(self.num1):
#             return self.num1 + self.num2

#     def sub(self):
#         return self.num1 - self.num2

#     def product(self):
#         return self.num1 * self.num2
#     #object is not passed through param
#     @staticmethod
#     def is_even_or_odd(num):
#         return num % 2 == 0
    
# calc  = Calculator(10, 5)
# print(Calculator.is_even_or_odd(5))
# print(calc.is_even_or_odd(10))
# # print(calc.add())
# print(calc.sub())
# print(calc.product())