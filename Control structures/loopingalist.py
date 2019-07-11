myList = ["book", "pencils", "horses", "red hair", "blonde", "mouse"]

lenMyList = len(myList)

# for loop

# for i in myList:
#     print(i)

# for i in range(lenMyList):
#     print(myList[i])

index = 0

# while index < lenMyList:
#     print(myList[index])
#     index += 1

while True:
    if index < lenMyList:
        print(myList[index])
        index += 1
    else: 
        break