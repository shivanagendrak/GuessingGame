import random
number=random.randint(1,20)
print("select the numbers from 1 to 20")
guess_number = int(input("Guess the Number: "))
count = 1
while guess_number!=number:
    if number<guess_number :
        print("Lower")
    else:
        print("Guess HIgher")
        
    guess_number = int(input("Guess the Number: "))
    count = count+1 
print("you guessed the Correct!")
print("You took",count,"attempts")