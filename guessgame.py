#guess game
import random
range = 50
guess = random.randint(1,50)
attempt = 0
n=5
print("hello user")
while attempt < 5:
    print("----------------------------------------------------------------------------")
    print("number of attempts remaining\n", n)
    value = int(input("enter a random number between 1->50 : \n"))
    if value > 50:
        print("anpadh range me daal")
    elif value == guess:
        print("correct in ",attempt+1," attempt\n")
        break
    elif value > guess:
        print("your guess is greater than computer's guess\n")
        attempt += 1
        n-=1
    else:
        print("your guess is lesser than computer's guess\n")
        attempt += 1
        n-=1 
else:
    print("beta tumse na ho payega {*<>*}\n")
    print("computer's guess id: ",guess)
