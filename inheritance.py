#inheritance = entities properties inherit or same
#characteristics reflect 
#eg = child inherits certain pro. parent(father / mother)
#inheritance = > proerties of class inherited by another class
#parent class => prperties/attributes => child class

#super class/ parent class
# class Animal:
#     def __init__(self,name,color):
#         self.species_name = name
#         self.color = color

#     def eat(self):
#         print(f"{self.species_name} is eating")
    
#     def run(self):
#         print(f"{self.species_name} is running")

# #sub class/ child class
# class Cat(Animal):
#     def __init__(self,name,color):
#         super().__init__(name,color) #parent class init function call

#     def grin(self):
#         print(f"{self.species_name} is grinnig.")

# #sub class/ child class
# class Dog(Animal):
#     def __init__(self,name,color):
#         super().__init__(name,color)




# c1 = Cat("tiger","red & black")
# d1 = Dog("Bull dog","brown")
# print(c1.species_name)
# d1.run()
# d1.eat()
# c1.grin()
# c1.run()

# tiger
# tiger is grinnig.
# tiger is running




# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#     #operator method overloading
#     def __eq__(self,object):
#         return self.price == object.price

#     def __add__(self,object):
#         return self.price + object.price

# pant = Product("Pant",2000)
# tshirt = Product("Tshirt", 2000)

# print(pant == tshirt) #=> False
# print(pant + tshirt) #=> error

#rule of inheritance
#child class "Is A" Parent class

# class Person: #parent/super class
#     def __init__(self,name):
#         self.name = name

#     def walk(self):
#         print(f"{self.name} is walking in parent class")
    
# class Student(Person): #child class/sub class
#     def __init__(self,name,age,address):
#         super().__init__(name)
#         self.age = age
#         self.address = address

#     def walk(self):
#         super().walk() #method overiding
#         print("walking in the student class")

#     def study(self):
#         print(f"{self.name} is studying at age {self.age}")



# st1 = Student("ram",20,"ktm")

# st1.walk()


# class Bird:
#     def __init__(self,name):
#         self.name = name

#     def fly(self):
#         print(f"{self.name} is flying in the parent class")

    
# class Eagle(Bird):
#     def __init__(self,name):
#         super().__init__(name)

    
# class Ostrish(Bird):
#     def __init__(self,name):
#         super().__init__(name)

#     def fly(self):
#         print(f"{self.name} canot fly from ostrich class")


# class HummingBird(Bird):
#     def __init__(self,name):
#         super().__init__(name)


#     def fly(self):
#         super().fly()
#         print(f"{self.name} can also fly backward")

# e1 = Eagle("Goblin")
# e1.fly()
# o1 = Ostrish("Peter")
# o1.fly()
# h1 = HummingBird("Mina")
# h1.fly()

#multiple behaviour in same method => polymorphism in oops


class Person:#parent
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def study(self):
        print(f"{self.name} is studying from Person class")

class Father(Person):#Child class
    def __init__(self,name,age):
        super().__init__(name,age)

    def work(self):
        print(f"{self.name} is working from Father class")

class Mother(Person):
    def __init__(self,name,age):
        super().__init__(name,age)

    def cook(self):
        print(f"{self.name} is cooking from Mother class")  


#multi level inheritance
class Student(Father,Mother):#grandChild class
    def __init__(self,name,age):
        super().__init__(name,age)
    

st1 = Student("ram",20)
st1.work()
# st1.study()
# st1.cook()
# print(Student.mro())

# ram is working from Father class
# ram is studying from Person class

