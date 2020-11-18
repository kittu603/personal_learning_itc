"""
Instance Method
Class Method
Static Method
"""
# Instance Method

#The purpose of instance methods is to set or get details about instances (objects),
# and that is why they’re known as instance methods.
# They have one default parameter- self
# Any method you create inside a class is an instance method unless you specially specify Python otherwise.


class MyClass:

    def __init__(self, a):
        self.a = a


    def instance_method(self):
        print(f"This is an instance method with parameter {self.a}")

    def get_class_name(self):
        print(f"I am from class: {self.__class__.__name__}")

obj = MyClass(10)
obj.instance_method()
obj.get_class_name()


# we CANNOT access the instance methods directly from class

#MyClass.instance_method() # TypeError: instance_method() missing 1 required positional argument: 'self'

# it is obvious because instance methods accept an instance of the class as the default parameter.
# And you are not providing any instance as an argument.
# Though this can be bypassing the object name as the argument:

#MyClass.instance_method(obj) #This is an instance method with parameter 10 >> WORKS as instance obj is passed :)

#USAGE

# The instance methods are the most commonly used methods.


print("********end********")

# Class Method

# The purpose of the class methods is to set or get the details (status) of the class.
# That is why they are known as class methods.
# They can’t access or modify specific instance data.
# They are bound to the class instead of their objects.
# In order to define a class method,
# you have to specify that it is a class method with the help of the @classmethod decorator
# Class methods also take one default parameter- cls,
# which points to the class. Again, this not mandatory to name the default parameter “cls”.
# But it is always better to go with the conventions
# Class methods can be accessed both by instances of class and as well as directly from class
class MyClass2:
    @classmethod
    def class_method(cls):
        print(f"i am from class method")
        print(f"I am from class: {cls.__name__}")

#accessing cls method via instances

obj2 = MyClass2
obj2.class_method()

#accessing cls method via Class
# we can access the class methods directly without creating an instance or object of the class

#MyClass2.class_method() #also prints same

class Animal:

    def __init__(self, name,color,age):
        self.name = name
        self.color = color
        self.age = age

    @classmethod
    def class_method(cls):
        print("This is class method")



    def run(self):
        print(f"{self.name} is running")

    def change_color(self,new_color):
        self.color = new_color


dog = Animal("ron",'blue',5)
# dog.run()
Animal.class_method()
# dog.class_method()

dog.change_color("red") # we can change instance state using instance method

# But class method cannot access or modify specific instance data
# means Cls method cannt access or modify self.name or similar instance attrs

# USAGE

# The most common use of the class methods is for creating factory methods.
# Factory methods are those methods that return a class object (like a constructor) for different use cases.

from datetime import date

class Dog:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def get_age_by_year(cls,name,year):
        return cls(name,date.today().year - year)


d = Dog('blue','2') #blue 2
print(d.name,d.age)

# below, we used cls method to create another cls object
d = Dog.get_age_by_year('blue',2009)
print(d.name,d.age) #blue 11

# Factory methods are those methods that return a class object (above)

print("********end********")


# Static Method

# Static methods cannot access the class data and instance data.
# In other words, they do not need to access the class data.
# They are self-sufficient and can work on their own.
# Since they are not attached to any class attribute,
# they cannot get or set the instance state or class state.


class MyClass3:

    @staticmethod
    def static_method():
        print("This is static method")
        print("I don't need neither class nor an instance")



# In order to define a static method,
# we can use the @staticmethod decorator
# (in a similar way we used @classmethod decorator).
# Unlike instance methods and class methods, we do not need to pass any special or default parameters.

obj3 = MyClass3
obj3.static_method()
MyClass3.static_method()


# we can call static methods from both class and instance
# but mind that we cannot change the state of class and instance
# these methods are used for creating utility functions.
# For accomplishing routine programming tasks we use utility functions

#USAGE

class Calculator:

    def __init__(self):
        self.buttons = 4

    def change_buttons(self, new_buttons):
        self.buttons = new_buttons

    @staticmethod

    def do_addition(x,y):
        print(x+y)
        try:
            print(f"{self.buttons}")

        except:
            print("cant get self.buttons from static method")


# Whenever you have to add two numbers,
# you can call this method directly without worrying about object construction.


Calculator.do_addition(10,20)
c = Calculator
c.do_addition(5,10)

#both of above works



















