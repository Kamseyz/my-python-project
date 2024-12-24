import sys

instruction = """ Please select the option:
1. Show-Balance
2. Tranfer
3. Exit
Select Option: """


def showbalance(balance):
    print (f"Your current balance is ${balance}")

def transfer (balance):
    username = input("Who do you want to transfer to: ")
    usercct = int(input("How much do you want to transfer: "))
    if usercct > balance:
        print ("Insufficent balance, try again! ")
        return balance
    else:
        balance -= usercct
        print (f"You successfully made a tranfer of ${usercct} to {username}")
        print(f"Your remaining balance is ${balance}")
        return balance
    
def main():
    balance = 10000
    while True:
        option = input(instruction)
        if option == "1":
            showbalance(balance)
        elif option == "2":
            balance = transfer(balance)
        elif option == "3":
            print("Good have a wonderful day!")
            sys.exit(0)
        else:
            print("Invalid option, select between 1,2 or 3")
main()