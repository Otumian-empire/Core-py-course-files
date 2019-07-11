# SOLUTION TO QUESTION 7 OF BASIC CONCEPTS ASSIGNMENT
# 7. write a python program to find the average of five integers and
# display the average (Take integers from user and Display only the
# integer part of the result)

# input: 5 integers from user
# output: average

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))
num5 = int(input("Enter the fifth number: "))

sumnum = num1 + num2 + num3 + num4 + num5

averagenum = int(sumnum / 5) #type cast because of int int division

print("The average of %d, %d, %d, %d and %d is %d" %(num1, num2, num3, num4, num5, averagenum))
# There are other ways to print out the output
