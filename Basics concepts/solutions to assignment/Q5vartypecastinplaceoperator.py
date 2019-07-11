# SOLUTION TO QUESTION 5 OF BASIC CONCEPTS ASSIGNMENT
# 5. Write python program that makes use of 3 variables, type casting and
# inplace operation

# Here you are to write any thing at all
# make use of 3 variables, type cast it and use inplace operation

# this is a program that takes the name of the user, age and height (3 vars)
# type casted the height
# 
# There are several ways to tackle this problem
name = input("Enter your name: ")
age = 27
height = float(input("Enter your height: "))

# ageplusheight = age + height can be written in a long format as the line below
ageplusheight = 0 #note that before you could use inplace operations, 
# var must have an initial val
age += height
ageplusheight += age

print("your name is ", name)
print("You are ", int(age), "years old and your height is ", height) 
#can you figure out why age is type casted/converted
print("Hoohoo, I had ", ageplusheight, "when i sumed your age and height")