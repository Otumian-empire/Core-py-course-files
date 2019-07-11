# if expression:
#     statement 1
# else:
#     statement 2

minor = eval(input("How old are you? "))

if minor < 18:
    print("I can't serve you alcohol")
else:
    if minor > 40:
        print("Hello oldie")
        
    print("What should i get you")
