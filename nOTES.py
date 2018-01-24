#import random
# #  Is this working
#
# print("Hello World")
# print("Welcome to class")
#
# # This is a comment.
# # I can use this to type in text
# # But it will never run
# '''This is a multi-line comment
# I wanted to type out a whole bunch
# but this is all
# text
# '''
#
# # Variables
# a=5
# b=4
# str1="The quick brown fox jumps over the lazy dog"
#
# print(str1)
#
# print(a+b)
# print(a-5*b)
# print(a*b)
# print(a/b)
# print(a**b)   # A to the power of B
#
#
# print(15 % 5)
# print(14 % 5)
# print(13 % 5)
# print(12 % 5)
# print(11 % 5)
# print(10 % 5)
# print(9 % 5)
# print(5 % 3)
#
#
# car_name = "Weibe Mobile"
# car_type = "Nissan GTR"
# car_cylinders = 8
# car_mpg = 9000.1
#
# # Inline printing
# print("I have a car called the %s" % car_type)
#
#
# def print_hw():
#     print("Hello World")
#
#     print_hw()
#     print_hw()
#     print_hw()
#
#
# def say_hi(name):
#     print("Hello %s." % name)
#     print("Enjoy your day.")
#
#
# say_hi("John")
#
#
# def print_age(name,age):
#     print("%s is %d year old." % (name, age))
#     age += 1  # age = + 1
#     print("Next year, they will be %d" % age)
#
#
# print_age ("John", 15)
# def f(x):
#     return x**3 +4 * x*82 +7 *x - 4
#
#
# print (f(3))
# print (f(4))
# print (f(5))
#
#
#  #If statement
#
#
# def grade_calc(percent):
#     if percent >= 90:
#         return "A"
#     elif percent < 90 and percent >=80 :
#         return "B"
#     elif percent >= 70:
#             return "C"
#     elif percent >= 60:
#         return "D"
#     elif percent >= 50:
#         return "E"
#     elif percent >= 40:
#         return "F"
#     elif percent >= 30:
#         return "G"
#     elif percent >= 20:
#         return "H"
#     elif percent >= 10:
#         return "I"
#
#
# '''Write a function called "happy_birthday"
# that "sings" (prints) Happy birthday
# '''
# def happy_bday(name):
#
#     print("Happy birthday to you")
#     print("Happy birthday to you")
#     print("Happy birthday to %s" % name)
#     print("Happy birthday to you")
#
# happy_bday("John")
#
#
#
# #Loops
#
# for num in range(10):
#     print(num + 100000)
#
# #loop
# a = 1
# while a <= 10:
#     print(a)
#     a += 1
#
#
# # Random Numbers
#
#
# import random  #This should be on line 1
# print(random.randint(0,100))
#
#
# # Comparisons
# print(1==1) # Is 1 equal to 1
# print(1 !=2) # Is 1 ntor equal to 2?
# print(10<= 15)
# print(not False)
#
# # Recasting
#
# c = '1'
# print(c == 1)   # Both are ints
# print(int(c) == 1)   #Gives a both are strings
#
# # The input command Always a string
#
#
# #Lists
the_count =[1,2,3,4,5]
shopping_list = ["Noodles","Eggrolls","Milk","rice","soda","chips"]

print(shopping_list[2])
print(len(shopping_list))

#Going through a list
for item in shopping_list :
    print(item)

for  num in the_count:
    print(num * 2)


len(shopping_list) #Gives length of the list
range(3) # Gives list of the number 0 through 2
range(len(shopping_list)) #A list of EVERY index in a list

for num in range(len(shopping_list)):
    item = shopping_list[num]
    print("The item at index %d is %s" % (num, item))

# Turn this into a list
str1 ="Hello Class!"
listOne = list(str1)
print(listOne)
listOne[11] = '.'
print(listOne)
print(listOne.join(""))



# Add things to a list
shopping_list.append("cereal")
print(shopping_list)

# Removing things from a list
shopping_list.remove("soda")
print(shopping_list)
shopping_list.pop(0)
print(shopping_list)

# the string class
import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.punctuation)
print(string.digits)

# Dealing with strings
strTwo = "ThIs iS a VeRY oDd sEnTenCE"
lowercase = strTwo.lower()