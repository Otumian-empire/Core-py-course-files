def greetings(name):
    print("Hello", name)

# greetings("Adom")

def add_two(param):
    param += 2
    print(param)

# add_two(23) 

def loop_to(stop):
    for i in range(stop): #[0,1,2,3,4]
        print("I am a loop", i)

# loop_to(5)

def paint(item, color):
    print("The " + item + " is " + color)

# paint("Car", "black")

def dgreetings(name="Mary"):
    print("Hello", name)

# dgreetings("cassie")

def dpaint(item, color="green"):
    print("The " + item + " is " + color)

# dpaint("car", "black")
# dpaint("Horse")


def dog_prof(name, age=2, color="brown", fav_food="pizza"):
    print("Hello, I am a dog")
    print("My name is " + name + " and i am " + str(age) + " years old.")
    print("I have " + color + " fur and I love " + fav_food)

# dog_prof("Scooby", fav_food="Rice ball", age=21)