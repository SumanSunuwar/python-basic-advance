# class => defence class

# property = gun, area(land,sky,sea)
# ABSTRACT = if common feature shared by all objects as they are

# from abc import ABC,abstractmethod

# class Father(ABC):

#     @abstractmethod
#     def disp(self): #abstract method
#         pass

#     def work(self):
#         print("working") #concrete method

# class Student(Father):
#     pass
#     #overiding of abstractmethod implementation compul.

#     def disp(self):
#         print(f"displaying in student class")


# st = Student()

# st.work()
# st.disp()

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def no_of_sides(self):
#         pass

# class Rectangle(Shape):

#     def no_of_sides(self):
#         print("I have four sides(rectangle")

# class Triangle(Shape):

#     def no_of_sides(self):
#         print("i have three side (triangle")

    
# t1 = Triangle()
# r1 = Rectangle()

# t1.no_of_sides()
# r1.no_of_sides()


# defence system => gun, area(land, sky, sea)

from abc import ABC, abstractmethod


class Defence(ABC):
    @abstractmethod
    def area(self):
        pass

    def gun(self):
        print("Gun : AK47")

class Army(Defence):
    def area(self):
        print("This is land defence system(Army)")

class Navy(Defence):
    def area(self):
        print("This is sea defence system(NAVY)")

class Airforce(Defence):
    def area(self):
        print("This is air defence system(AIRFirce)")

a = Army()
n = Navy()
af = Airforce()

a.gun()
n.gun()
af.gun()
a.area()
n.area()
af.area()  

print("method finished executing")
