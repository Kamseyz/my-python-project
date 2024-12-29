import random



def entervalue1():
    while True:
        enterValue = input("Roll a dice (Y/N): ").strip().upper()
        if enterValue == "Y":
           a =(random.randrange(1,6))
           b= (random.randrange(1,6))
           result = (a, b)
           print (result)
        elif enterValue== "N":
           print("No Problem, Goodbye! ")
           break
        else:
            print("Invalid keyword, try again")


#call function
entervalue1()


# print(random.randint(1, 10))  # Output: A random integer between 1 and 10
