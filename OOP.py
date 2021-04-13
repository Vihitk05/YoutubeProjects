"""

    #OOP (Object Oriented Programming) Concepts
    Python is not an "OBJECT ORIENTED LANGUAGE". The reason behind this is the
    creator of Python "Guido Van Russom" wanted to keep things simple and avoid
    data hiding.But, yes Python supports some of the basic features of OOP.
    OOP is supported by JAVA,C++,JavaScript,etc. So, we'll be exploring some
    of the features in OOP.

"""

"""

    #Classes
    Classes are basically used to create new Types.

    #Objects
    Its an instance variable used to call out a class.

    #Constructors
    This method is used to construct or create a new object.

    #Inheritance
    This is used when a particular method is repeated in different classes.
    By using inheritance we can inherit all the methods of a class to another.

"""


class TvRemote:
    def __init__(self, ok_index, back_index):
        self.ok_index = ok_index
        self.back_index = back_index

    def ok(self):
        print('Ok!')

    def back(self):
        print('Back!')


# Object      Arguments
tv = TvRemote(12, 23)
print(tv.ok_index)  # printing the attribute
tv.ok_index = 13  # Updating the attribute
tv.ok()  # Calling the method of class TvRemote


# INHERITANCE
class Fruit:
    def is_fruit(self):
        print(True)


class Banana(Fruit):  # Methods Inherited in class Banana
    def taste(self):
        print('Sweet')


class Lemon(Fruit):  # Methods Inherited in class Lemon
    def taste(self):
        print('Sour')


fruit1 = Banana()
fruit1.is_fruit()  # Calling the Inherited Method

fruit2 = Lemon()
fruit2.is_fruit()  # Calling the Inherited Method

fruit3 = Banana()  # fruit1 and fruit3 are different objects
