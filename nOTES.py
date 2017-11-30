import random
#  Is this working

print("Hello World")
print("Welcome to class")

# This is a comment.
# I can use this to type in text
# But it will never run
'''This is a multi-line comment
I wanted to type out a whole bunch
but this is all
text
'''

# Variables
a=5
b=4
str1="The quick brown fox jumps over the lazy dog"

print(str1)

print(a+b)
print(a-5*b)
print(a*b)
print(a/b)
print(a**b)   # A to the power of B


print(15 % 5)
print(14 % 5)
print(13 % 5)
print(12 % 5)
print(11 % 5)
print(10 % 5)
print(9 % 5)
print(5 % 3)


car_name = "Weibe Mobile"
car_type = "Nissan GTR"
car_cylinders = 8
car_mpg = 9000.1

# Inline printing
print("I have a car called the %s" % car_type)


def print_hw():
    print("Hello World")

    print_hw()
    print_hw()
    print_hw()


def say_hi(name):
    print("Hello %s." % name)
    print("Enjoy your day.")


say_hi("John")


def print_age(name,age):
    print("%s is %d year old." % (name, age))
    age += 1  # age = + 1
    print("Next year, they will be %d" % age)


print_age ("John", 15)
def f(x):
    return x**3 +4 * x*82 +7 *x - 4


print (f(3))
print (f(4))
print (f(5))


 #If statement


def grade_calc(percent):
    if percent >= 90:
        return "A"
    elif percent < 90 and percent >=80 :
        return "B"
    elif percent >= 70:
            return "C"
    elif percent >= 60:
        return "D"
    elif percent >= 50:
        return "E"
    elif percent >= 40:
        return "F"
    elif percent >= 30:
        return "G"
    elif percent >= 20:
        return "H"
    elif percent >= 10:
        return "I"


'''Write a function called "happy_birthday"
that "sings" (prints) Happy birthday
'''
def happy_bday(name):

    print("Happy birthday to you")
    print("Happy birthday to you")
    print("Happy birthday to %s" % name)
    print("Happy birthday to you")

happy_bday("John")



#Loops

for num in range(10):
    print(num + 100000)

#loop
a = 1
while a <= 10:
    print(a)
    a += 1


# Random Numbers


import random  #This should be on line 1
print(random.randint(0,100))
