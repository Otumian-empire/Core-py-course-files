# SOLUTION TO QUESTION 7 OF BASIC CONCEPTS ASSIGNMENT
# 10. write a program to compute the area of a circle, taking the radius from the user. Display the radiu, and the area (pi = 3.142)

# input: pi, radius (float)
# otuput: area (float), area = pi * radius square (radius square = radius * radius or radius ** 2)
# There might be another way to write this program

pi = 3.142
radius = float(input("Enter the radius of the circle: "))
areaofcircle = pi * (radius ** 2)

print("The area of circle of radius, %.2fcm is %.2fcm sq unit" %(radius, areaofcircle))
