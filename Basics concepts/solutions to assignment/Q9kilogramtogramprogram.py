# SOLUTION TO QUESTION 7 OF BASIC CONCEPTS ASSIGNMENT
# 9. write a program that takes input from the user as kilogram. convert
# the kilogram to gram and display the result

# input: kilogram, float
# output: gram, float
# 1kg = 1000g, to convert to gram, divide by 1000

kilogram = float(input("Enter mass in kilogram: "))
gram = float(kilogram / 1000)

print("%.2fkg is equivalent to %.2fg" %(kilogram, gram))