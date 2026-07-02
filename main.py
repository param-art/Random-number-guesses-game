import random
while(True):
    computer = random.randint(1,50)
    for i in range(1,9):
        you = int(input("Enter your number : "))
        if computer == you:
            print(f"Your number is {computer}")
            break
        else:
            if computer < you :
                print("the number is too high")
            elif computer > you:
                print("the number is too low")
            else:
                print("Game over ")
            #the number of guesses left
            print(f"guesses left : {8-i}")

    print(f"the answer is {computer}")
          
    if computer!=you:
        print("Game over")
    print("want to retry")
    retry = input("Enter y/n : ").lower()
    if retry != "y":
        break