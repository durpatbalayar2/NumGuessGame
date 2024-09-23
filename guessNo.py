#Number Guessing Game

import random

# Ask Player to choose lvs
print("****Choose a level, You want to play:***")
print("\n1. Easy mode(1-50, Unlimited attempts)")
print("2. Medium mode( 1-100),10 attempts")
print("3. Hard mode(1-500),5 attempts")

level=int(input("\nEnter 1 2 or 3 to choose a level:"))

# set Target Number & Attempts
if level== 1:
    target=random.randint(1,50)
    max_attempts = None  # Unlimited attempts
    print("You have choose easy mode.Good luck!!")
    
elif level==2:
    target=random.randint(1,100)
    max_attempts=10
    print("Medium mode selected.You have 10 attempts!!")
    
elif level==3:
    target=random.randint(1,500)
    max_attempts=5
    print("Hard Mode selected. Be careful only 5 attempts you will get.")
    
else:
    print("Invalid choice !  Defaulting to easy mode!!!") 
    target = random.randint(1, 50)
    max_attempts = None
    
# game loop with attempt counter

attempts = 0 # start counting attempts
while True:
    if max_attempts is not None and attempts >= max_attempts:
        print("You have used all atempts. Game Over !!!")
        break
    
    user_input= input("Guess the target number or type 'quit' to exit.")
    
    if user_input.lower() == 'quit':
        print("Thanks for playing.See You Again !!.")
        break
    
    guess = int(user_input)
    attempts += 1  # Increment the attempt count
    
    
# Check if the Guess is Correct with limited attempts 
    if guess == target:
        print("Congratulation! You sucessfully guess the correct number in",attempts,"attempts.")
        break
    elif(guess< target):
        print("Your guess is too low. Try guess a bigger number")
    else:
        print("Your guess is too big. Guess a small one") 
    
    if max_attempts is not None:
        print("You have ",max_attempts - attempts,"attempts remaining.")
        
print("----Game Over---")               
                   


