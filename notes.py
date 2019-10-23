


# #                                   NUMBERS
#
#
# # addition
# a = 2+1
#
# # subtraction
# b = 2-1
#
# # multiplication
# c = 2*2
#
# # division
# d = 4/2
#
# # powers
# e = 2**5
#
# # square root
# f = 4**0.5
#
# # order of operations is maintained by parenthesis
# g = (2+10) * (10+3)
#
# # variables can also have operations or be seperated by commas
# print(a+b*c-d**e/f)
# print(a,b,c,d,e,f)
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
#
# # to run simply enter file path in python terminal terminal I.E. numbers.py
#
# # Number Objects
# my_income = 1000
# tax_rate = 0.1
# my_taxes = my_income * tax_rate
# print(my_taxes)

# #                                STRINGS
#
#
#                                 # basics
# a = "string"
# b = 'string'
# c = "string's"
# d = '"string"'
#
# print(a,b,c,d)
#
#                                 # indexing
#
# # individual characters can be selected by index
# print(a[2], b[-1])
#
# # slicing
# # for everything after a certain index point in a string
# print(c[2:])
#
# # for everything up to index 2
# print(c[:2])
#
# # for a section between index 2 and index 5
# print(c[2:5])
#
# # to return everything in a string
# print(c[:])
#
# # define a step size
# # [1] returns everything [2] returns every other [3] returns every third
# # ...and so on
# print(c[::3])
#
#
#                             # basic methods
#
# string_a = 'abcdefghij'
# string_b = 'ABCDEFGHIJ'
# string_c = 'two words'
#
# # make a string all uppercase
# a = string_a.upper()
# print(a)
#
# # make a string all lowercase
# b = string_b.lower()
# print(b)
#
# # to capitalize first letter of strings
# c = string_a.capitalize()
# print(c)
#
# # split a string by spaces
# d = string_c.split()
# print(d)
#
# # or split by character, also removing that character
# e = string_c.split('o')
# print(e)
#
#                         # print formatting
#
# # string interpolation "THE TURDUCKEN OF STRINGS"
# inter = "insert another string here: {}".format("INSERT ME")
# print(inter)
#
# # for multiple inserts
# multi_inter = "Item one: {} Item Two: {}".format("FIRST", "SECOND")
# print(multi_inter)
#
# # or use variables for insertion (most common)
# multi_inter_var = "Item one: {x} Item Two: {y}".format(x = "FIRST", y = "SECOND")
# print(multi_inter_var)

#
#
#                                 # lists
#
# # a python list looks a lot like a js array
# mylist1 = [4,5,6]
#
# # they can be made up of multiple data types
# mylist2 = ['string', 1,2,3,23.2,True,'asdf',[1,2,3], mylist1]
# print(mylist2)
#
# # for length of a list
# print(len(mylist1))
#
# # indexing works the same as with strings
# print(mylist1[1])
#
# # also same with slicing
# print(mylist2[1:5])
#
#
#
# # MUTABILITY! the benefit of lists...Things cna be added and removed
#
# # replaces 'a' with 'NEW ITEM'
# mylist3 = ['a', 'b', 'c', 'd', 'e']
# print('before reassignment')
# print(mylist3)
# mylist3[0] = 'NEW ITEM'
# print("after reassignment:")
# print(mylist3)
#
#
#
# # BASIC LIST METHODS
#
# # To append an item to the end of a list
# mylist3.append('f')
#
# # does not combine Lists
# mylist3.append(['x', 'y', 'z'])
#
# # for this, use .extend
# mylist3.extend(['x', 'y', 'z'])
#
# # to remove last item
# item = mylist3.pop()
# print(mylist3)
# # call item to select removed item
# print(item)
#
# # to pop specific item, use index number
# item2 = mylist3.pop(2)
# print(mylist3)
#
# # reverse a list
# reverse = mylist3.reverse()
# print(mylist3)
#
# # sort a random order of numbers
# num_list = [3,6,5,8,1,4,7,9,2]
# num_list.sort()
# print(num_list)
#
#
#
# # nested list indexing
# num_list2 = [1,2,['x','y','z']]
# print(num_list2[2][1])
#
#
#
# # list comprehension
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
#
# # counts as first item in first list
# print(matrix[0][0])
#
# # for second item
# print(matrix[0][1])
#
# # for loop in lists to print first index of each list as a list itself
# first_col = [row[0] for row in matrix]
# print(first_col)
#


# #                               DICTIONARIES
#
# # same as an object
# my_stuff = {"key1":"value1", "key2":"value2"}
#
# # DICTIONARIES DO NOT RETAIN ORDER LIKE LISTS OR STRINGS DO
# my_stuff2 = {"name":"Joshua","age":38,"courses":{"python":[1,2],"JavaScript":[1,2,3]}}
#
# # to grab a specific key value
# print(my_stuff["key2"])
#
# # to select from nested dictionaries
# print(my_stuff2["courses"]["JavaScript"][2])
#
# # changing key values
# my_stuff3 = {'lunch':'pizza', 'dinner':'pasta'}
# my_stuff3['lunch'] = 'burger'
#
# # adding new keys
# my_stuff3['breakfast'] = 'oatmeal'
#
# print(my_stuff3)


# #                              Tuples
# # immutable sequences, basically a list that cannot be altered
# t = (1,2,3)
# print(t[2])
#
# #                               Sets
# # unordered collections of unique elements
# x = set()
#
# x.add(1)
# x.add(2)
# x.add(1.76)
# x.add(200)
# print(x)
#
# # convert a list into a set to avoid repeat elements
# converted = set([1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3,3,4,4,4,4,4,5,5,5])
# print(converted)
#
#
# #                             Booleans
# True
# False
# # not commonly but sometimes also...
# 0
# 1

#
#
#
#
# #                            Control flow
#
# # logical operators
#
# # and
# (3 > 2) and (2 < 3)
#
# # or
# (3 > 2) or (2 < 3)
#
# # logic statements, indentaation matters
# # if statements
# if 1 < 2:
#     print('First Block')
#     if 20 > 3:
#         print('Second Block')
#
# # if, else and elif (else if)
# if 3 < 2:
#     print("if")
# elif 3 == 3:
#     print('elif')
# else:
#     print("else")
#
# # for loops in a list
# seq = [1,2,3,4,5,6]
#
# for item in seq:
#     print('hello')
#     print(item)
#
# # for loops in a dictionary
# d = {"sam":1, "frank":2, "dan":3}
#
# for item2 in d:
#     # for just keys
#     print(item2)
# # if you want value...
# for k in d:
#     print(d[k])
#
#
# # tuple iteration
# mypairs = [(1,2),(3,4),(5,6)]
#
# # tuple unpacking
# for (tup1, tup2)  in mypairs:
#     # prints first character in each tuple
#     print(tup1)
#     # prints second character in each tuple
#     print(tup2)
#
#
# # while loops
# i = 1
#
# while i < 5:
#     print("i = {}".format(i))
#     i = i + 1
#
#
# # range functions
# # quickly generate integers based on starting point and ending point
# print(range(5)) # range(0, 5)
# print(list(range(0,5))) # [0, 1, 2, 3, 4]
# print(list(range(0,20,2))) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
#
# for item3 in range(10):
#     print(item3)
#
#
# # deeper list comprehension
# j = [1,2,3,4]
#
# out = []
# for num in j:
# # print each ineger to the power of 2
#     out.append(num**2)
# print(out)
#
# # with the same output
# out = [num**2 for num in j]
# print(out)
#
#
#
# #                               Functions
#
# def my_func(param1 = "default value"):
#     # for docstring comments
#     """
#     THIS IS THE DOCSTRING
#     """
#     print("my first python function! {}".format(param1))
#
# print(my_func()) #....or
#
#
#
#
# def hello():
#     # print("hello")
#     return "hello"
#
# result = hello()
#
# print(result)
#
#
# def add_num(num1, num2):
#     # this if statement will check for integrs versus strings
#     if type(num1)==type(num2)==type(10):
#         return num1 + num2
#     else:
#         return "Sorry, I need integers!"
#
# result = add_num("2","3") # 23
# result = add_num(2,3) # 5
#
# # shows class type
# # print(type(result))
#
# print(result)
#
#
# # LAMBDA EXPRESSIONS
#
# for functions that except other functions as input parameters
# ....such as
#
# # filter functions
# mylist4 = [1,2,3,4,5,6,7,8]
#
# def even_bool(num):
#     return num % 2 == 0
# filter only is a generator and must be called after it's established
# evens = filter(even_bool,mylist4)
# to print out all even numbers in mylist4
# print(list(evens))
#
# # FOR THIS TO BE A LAMBDA EXPRESSION, no name is required
# evens = filter(lambda num:num % 2 == 0, mylist4)
# print(list(evens))
#
#
#
# # Useful additional METHODS
#
# # for STRINGS
# st = "hElLo"
#
# st.upper()
# st.lower()
# st.capitalize()
# st.count()
# st.split()


# #                            Scope
#
#
# # Python scope follows the LEGB rule
#     # ~ Local
#     # ~ Enclosing function locals
#     # ~ Global
#     # ~ Built-in
# # LEGB is the order in which Python looks up a variable name
#
# # L: Local = Names assigned in any way within a function
# # yet not declared in that function
#
# # E: (E.F.Ls) = name in local scope of any and all enclosing
# # functions from inner to outer
#
# # G: Global (module) = names assigned at the top level of a
# # module or file, or declared global in a def within a file
#
# # B: Built-in = names preassigned in the built-in names module:
# # open, renge, SyntaxError,...
#
# #######################
#
# x = 25
#
# def my_func():
#     x = 50
#     return x
#
# # print(x)
# # print(my_func())
#
# my_func()
# # x = 25 is global, x = 50 is local to my_func
# print(x) # this still prints 25 because 50 only exists within my_func
#
# #######################
#
# # Local
# lambda x: x**2
#
# #######################
#
#
# # Enclosing function locals
# name = "This is a global name!"
#
# def greet():
#     name = "sammy"
#
#     def hello():
#         print("hello "+name)
#
#     hello()
#
# greet()
# print(name)
#
# #######################
#
# # ADDITIONAL EXAMPLE
# x = 50
#
# def func(x):
#     print('x is: ',x)
#     x = 1000
#     print('local x is changed to: ',x)
#
# func(x) # output = function output
# print(x) # output = 50
#
#
# #######################
#
# # TO MAKE print(x) RETURN 1000 YOU MUST MAKE A global CALL...
# # This makes the new value of x permenant
#
# x = 50
#
# def func():
#     global x
#     x = 1000
#
# print("before function call, x is: ",x) # 50
# func()
# print("after function call, x is: ",x) # 1000



# #                      OBJECT ORIENTED PROGRAMMING 1 - 2
#
# #                                  classes
#
# # How can I make this a list object?
# mylist = [1,2,3]
# mylist.append(4)
# print(mylist) # [1,2,3,4]
# # ...in Python, everything is an OBJECT
#
# # to find out what type simply...
# print(type([1,2,3])) # <class 'list'>
#
# # A class in Python is simply a blueprint that defines
# # the nature of a future object
#
# # with an object you can create instances of a class
#
# #######################
#
# # an instance is just a specific object created from a particular class
#
# # note that class name are always capitalized
# class Sample():
#     pass
#
# x = Sample()
# print(type(x)) # <class '__main__.Sample'>
#
# #######################
#
# # attributes - characteristics of an object
#
# # methods - operations you can perform on an object
#
# class Dog():
#
#     def __init__(self): # most basic "special method"
#         pass
#
# mydog = Dog()
# print(type(mydog))
#
# #######################
#
#
# # to apply attributes
#
# class Dog():
#
#     def __init__(self,breed,name): # now add more attributes after self
#         self.breed = breed
#         self.name = name
#
# mydog = Dog(breed = "Lab", name="Nova") # this now requires a breed attribute
#
# # you can now craete other instances with the breed attribute
# otherdog = Dog("Huskie","Fido") # attribute play out in order so no need
# # to actually label them
#
# print(mydog.name, mydog.breed) # Nova Lab
# print(otherdog.name, otherdog.breed) # Fido Huskie
# # notice no closed parenthesis after attributes
#
#
# #######################
#
# class Dog():
#
#     # class object attributes
#     species = "canine" # remains true
#
#     def __init__(self, breed, name): # most basic "special method"
#         self.breed = breed
#         self.name = name
#
# mydog = Dog("Husky", "Nova") # notice species is not called here
# print(mydog.species, mydog.breed, mydog.name) # canine Husky Nova
#
# #######################
#
# class Circle():
#
#     pi = 3.14
#     def __init__(self,radius=1): # the radius attribute has a default
#     # parameter value of 1
#         self.radius = radius
#
# myc = Circle()
# print(myc.radius) # 1
#
# #######################
#
#
# # METHODS ( performed inside the body of a class )
# class Circle():
#
#     pi = 3.14
#     def __init__(self,radius=1):
#         self.radius = radius
#
#     def area(self):
#         return self.radius*self.radius * Circle.pi
#
# myc = Circle(3)
# # print(myc.radius) # 3
# print(myc.area()) # 28.26
# # note that area is not a class so it is called like a function, with ()
#
# #######################
#
# # there are 2 ways of changing attributes of a class...
#
# class Circle():
#
#     pi = 3.14
#     def __init__(self,radius=1):
#         self.radius = radius
#
#     def area(self):
#         return self.radius*self.radius * Circle.pi
#
#     # if you want a method that will reset attribute values
#     def set_radius(self,new_r):
#         self.radius = new_r
#
# myc = Circle(3)
# # myc.radius = 100 # you can just do this without a method
#
# # to use set_radius method
# myc.set_radius(999)
#
# print(myc.area()) # 3133723.14
#
# #######################
#



# #                      OBJECT ORIENTED PROGRAMMING 3
#
#
# #  two types of classes, derived-classes and base-classes
# # derived-classes are derived from a base-class
#
#
# #######################
#
# # INHERITANCE...
#
# # EXAMPLE OF A BASE CLASS
# class Animal():
#
#     def __init__(self):
#         print("ANIMAL CREATED")
#
#     def whoAmI(self):
#         print("ANIMAL")
#
#     def eat(self):
#         print("EATING")
#
# # to inherit from the base class of Animal() in a new class
# class Dog(Animal): # pass in the animal class
#
#     def __init__(self):
#         # Animal.__init__(self)
#         print("DOG CREATED")
#
#     # new methods can also be created within Dog()...
#     def bark(self):
#         print("Woof!")
#
#     # methods can also be redefined...
#     def eat(self):
#         print("Dog eating!")
#
#
# # NOTE: no need to type print because print is part of each function
# mydog = Dog() # DOG CREATED
# mydog.whoAmI() # ANIMAL
# mydog.eat() # Dog eating!
# mydog.bark() # Woof!
#
# #######################
#
#
# # SPECIAL METHODS
#
# # these allow you to perform special operations
# # they are not called directly, but through special syntax
#
# # EXAMPLE:
# class Book():
#
#     def __init__(self,title,author,pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     # this is one of the most commonly used special methods
#     def __str__(self): # __str__ represents the string version of an object
#
#         # use print formatting to call information
#         return "Title: {}, Author: {}, Pages {}".format(self.title,self.author,self.pages)
#
#     # another special method is __len__
#     def __len__(self):
#         return self.pages
#
#     # and yet another?...there are many!
#     def __del__(self):
#         print("the book is destroyed!")
#
#
# b = Book("Python","Joshua",200)
# print(b) # Title: Python, Author: Joshua, Pages 200
# print(len(b)) # 200
#
# del b # the book is destroyed!
# print(b) # NameError: name 'b' is not defined


# #                   Errors and Exceptions
#
# # how to setup your own ERROR and EXCEPTION calls
#
# # these are the keywords to use
# # to dictate our logic in case of an error
#
# # Try
# # Except
# # Finally
#
# # we will be opening files to show this in action
# # to do so, use the...  open("myfile.txt", "r")  ... function
#
# # Exceptions are errors that occur during the execution of code
#
# # you can use the 3 keywords abaove to dictate how these errors are
# # actually handled
#
# # here is the syntax:
#
# # try:
# #     operation goes here...
# #     ...
# # except Exception1:
# #     If there is an Exception1, then execute this block.
# # except Exception2:
# #     If there is Exception2, then execute this block.
# #     ...
# # else:
# #     If there is no exception, execute this block
#
# ##########################
#
#
# # Real EXAMPLE:
#
# try:
#     f = open("simple.txt", "w") # no error
#     # f = open("simple.txt", "r") # returns custom error
#     f.write("Test write to simple text!")
# except IOError:
#     print("ERROR: COULD NOT FIND FILE OR READ DATA")
# else:
#     print("SUCCESS!")
#     f.close()
#
# ##########################
#
#
# # to add in the "finally" keyword
#
# try:
#     f = open("simple.txt", "r")
#     f.write("Test write to simple text!")
# except:
#     print("ERROR: COULD NOT FIND FILE OR READ DATA")
# finally:
#     print("FINALLY, always works!")


#
#
# #                            REGULAR EXPRESSIONS
#
# import re # "re" is for "Regular Expressions"
#
#
# patterns = ['term1', 'term2']
#
# text = 'This is a string with term1, but not the other! '
#
# for pattern in patterns:
#     print("I'm searching for: "+pattern)
#
#     if re.search(pattern,text):
#         print("Match!")
#     else:
#         print("No Match!")
#
#
# ##########################
#
#
# text = 'term1'
#
# match = re.search('term1',text)
#
# # print(type(match))
# print(match.start()) # 0, because the pattern term1 sarts at index 0
#
#
# ##########################
#
#
# split_term = "@"
#
# email = "user@email.com"
#
# print(re.split(split_term,email)) # ['user', 'email.com']
#
#
# ##########################
#
#
# print(re.findall('match','test phrase match in match middle')) # ['match', 'match']
#
#
# ##########################
#
#
#
#
# #                           REPETITION SYNTAX
#
#
# def multi_re_find(patterns,phrase):
#
#     for pat in patterns:
#         print("Searching for pattern {}".format(pat))
#         print(re.findall(pat,phrase))
#         print('\n')
#
#
# test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'
#
#
#
# # find an s with zero or more d's following it...
# test_patterns = ['sd*'] # output below
#
# # ['sd', 'sd', 's', 's', 'sddd', 'sddd', 'sddd', 'sd', 's', 's', 's', 's', 's', 's', 'sdddd']
#
#
# # for s with one or more d's following it...
# test_patterns = ['sd+'] # output below
#
# # ['sd', 'sd', 'sddd', 'sddd', 'sddd', 'sd', 'sdddd']
#
#
# # for s with zero to one d's following...
# test_patterns = ['sd?'] # output below
# # ['sd', 'sd', 's', 's', 'sd', 'sd', 'sd', 'sd', 's', 's', 's', 's', 's', 's', 'sd']
#
#
# # for s with a specified number of d's following...
# test_patterns = ['sd{3}'] # output below
# # ['sddd', 'sddd', 'sddd', 'sddd']
#
#
# # for s with two specified numbers of d's following...
# test_patterns = ['sd{1,3}'] # output below
# # ['sd', 'sd', 'sddd', 'sddd', 'sddd', 'sd', 'sddd']
#
#
# # for s with one or more s's or d's following...
# test_patterns = ['sd[sd]+'] # output below
# # ['sdsd', 'sddd', 'sdddsddd', 'sds', 'sdddd']
#
#
# ##########################
#
#
# def multi_re_find(patterns,phrase):
#
#     for pat in patterns:
#         print("Searching for pattern {}".format(pat))
#         print(re.findall(pat,phrase))
#         print('\n')
#
#
# test_phrase = 'This is a string! But it has punctuation and numbers 12345. How can we remove it?'
#
# # the ^ symbol indicates remove what symbols follow it if they occurs in the string
# test_patterns = ['[^!.?]+'] # output below
# # ['This is a string', ' But it has punctuation and numbers 12345', ' How can we remove it']
#
#
# # show only lowercase letters
# test_patterns = ['[a-z]+'] # output below
# # ['his', 'is', 'a', 'string', 'ut', 'it', 'has', 'punctuation', 'and', 'numbers', 'ow', 'can', 'we', 'remove', 'it']
#
#
# # show the numbers in a string '/d+' means show all digits, 'r' is for read
# test_patterns = [r'\d+'] # output below
# # ['12345']
#
#
# # show all non digits with '/D+'
# test_patterns = [r'\D+'] # output below
# # ['This is a string! But it has punctuation and numbers ', '. How can we remove it?']
#
#
# # show all white space with '/s+'
# test_patterns = [r'\s+'] # output below
# # [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
#
#
# # show all non-white space with '/s+'
# test_patterns = [r'\S+'] # output below
# # ['This', 'is', 'a', 'string!', 'But', 'it', 'has', 'punctuation', 'and', 'numbers', '12345.', 'How', 'can', 'we', 'remove', 'it?']
#
#
# # show all alpha/numeric characters
# test_patterns = [r'\w+'] # output below
# # ['This', 'is', 'a', 'string', 'But', 'it', 'has', 'punctuation', 'and', 'numbers', '12345', 'How', 'can', 'we', 'remove', 'it']
#
#
# # show all non-alpha/numeric characters
# test_patterns = [r'\W+'] # output below
# # [' ', ' ', ' ', '! ', ' ', ' ', ' ', ' ', ' ', ' ', '. ', ' ', ' ', ' ', ' ', '?']
#
#
#
#
# multi_re_find(test_patterns,test_phrase)

#
#
#
# #                            DECORATORS
#
# #############################
#
# def hello(name="josh"):
#     print("THE HELLO() FUNCTION HAS BEEN RUN!")
#
#     def greet():
#         return "THIS STRING IS INSIDE GREET()"
#
#     def welcome():
#         return "THIS STRING IS INSIDE WELCOME!"
#
# # CALLING GLOBAL VARIABLES
# hello() # THE HELLO( FUNCTION HAS BEEN RUN!)
#
# #############################
#
# # If you want to call local variables within the scope of a function
#
# def hello(name="josh"):
#     print("THE HELLO() FUNCTION HAS BEEN RUN!")
#
#     def greet():
#         return "THIS STRING IS INSIDE GREET()"
#
#     def welcome():
#         return "THIS STRING IS INSIDE WELCOME!"
#
#     print(greet())
#     print(welcome())
#     print("End of hello()")
#
# hello() # THE HELLO() FUNCTION HAS BEEN RUN!
# #         THIS STRING IS INSIDE GREET()
# #         THIS STRING IS INSIDE WELCOME!
# #         End of hello()
#
# #############################
#
#
# def hello(name="josh"):
#     print("THE HELLO() FUNCTION HAS BEEN RUN!")
#
#     def greet():
#         return "THIS STRING IS INSIDE GREET()"
#
#     def welcome():
#         return "THIS STRING IS INSIDE WELCOME!"
#
#     if name == "jose":
#         return greet
#     else:
#         return welcome
#
# x = hello()
#
# print(x()) # THE HELLO() FUNCTION HAS BEEN RUN!
# #            THIS STRING IS INSIDE WELCOME!
#
# #############################
#
# def hello():
#     return "Hi Joshua!"
#
# def other(func):
#     print("HELLO")
#     print(func())
#
# other(hello) # HELLO
# #              Hi Joshua!
#
# #############################
#
#
# def new_decorator(func):
#
#     def wrap_func():
#         print("CODE HERE BEFORE EXECUTING FUNC")
#         func()
#         print("FUNC() HAS BEEN CALLED")
#
#     return wrap_func
#
# def func_needs_decorator():
#     print("THIS FUNCTION NEEDS A DECORATOR!")
#
# # func_needs_decorator() # THIS FUNCTION NEEDS A DECORATOR!
#
# func_needs_decorator = new_decorator(func_needs_decorator)
# func_needs_decorator() # CODE HERE BEFORE EXECUTING FUNC
# #                        THIS FUNCTION NEEDS A DECORATOR!
# #                        FUNC() HAS BEEN CALLED
#
#                 ################
#                 # ALTERNATIVLY #
#                 ################
#
# def new_decorator(func):
#
#     def wrap_func():
#         print("CODE HERE BEFORE EXECUTING FUNC")
#         func()
#         print("FUNC() HAS BEEN CALLED")
#
#     return wrap_func
#
# # YOU CAN ALSO USE THE @ SYMBOL
# @new_decorator # is equal- to func_needs_decorator = new_decorator(func_needs_decorator)
# def func_needs_decorator():
#     print("THIS FUNCTION NEEDS A DECORATOR!")
#
# func_needs_decorator() # CODE HERE BEFORE EXECUTING FUNC
# #                        THIS FUNCTION NEEDS A DECORATOR!
# #                        FUNC() HAS BEEN CALLED
#
# # NOTE: output is the same
#
# #############################















#
