# SOLUTION TO QUESTION 8 OF BASIC CONCEPTS ASSIGNMENT
# 8. Write a program that prompts the user to input a decimal number and
# outputs the number to the nearest integer.

# input: float val
# output: int val by type cast

floatvar = float(input("Enter a decimal number: "))
intvar = int(floatvar)
print("%f to the nearest integer is %d" %(floatvar, intvar))