'''
class Student:
    def __init__(self):
        self.name = "Rapol"
        self.grades = (70,90,80,100)
    def average(self):
        return sum(self.grades) / len(self.grades)

student = Student()
print(student.name)
#must create an variable which has return value of class 
print(student.average())

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    def average(self):
        return sum(self.grades) / len(self.grades)

student = Student("rapol", (70,90,80,100))
print(student.name)
#must create an variable which has return value of class 
print(student.average())

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
#Returning init method will always return a memory not a value
    def __str__(self):
        return f"{self.name} person age is {self.age}"
#use __str__ to get value of an object or a string(representing an object as a string)
bob = Person("bob", 35)
print(bob)

#all functions inside the class that use the object as first parameter called instance
class ClassTest:
    def instance_method(self):
        print(f"{self}")
    @classmethod
    def class_method(cls):
        print(f"{cls}")

#test = ClassTest
#print(test.instance_method)
#instance method requires object to call them

ClassTest.class_method()
'''
class Books:
    Types = ("hardcover", "paperback")
    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight 
    def __repr__(self):
        return f"Book {self.name}, {self.book_type}, weight {self.weight}"

    @classmethod
    def hardcover(cls, name, page_weight):
        return Books(name, Books.Types[0], page_weight)


book = Books.hardcover("harryporter", 1000)
print(book)