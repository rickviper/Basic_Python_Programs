#Number guessing game using Random
import random

secNo = random.randint(1, 10)
attempts = 0
maxattempts = 3
print("Welcome to the guessing game. I am thinking of a number between 1 and 10, guess the correct number in 3 attempts. Good Luck!")
while attempts < maxattempts and attempts != maxattempts:
    guessed_num = int(input("Enter your guess: "))
    if guessed_num == secNo:
        print(f"Congrats you guessed the number {secNo}!!!!")
        break
    elif guessed_num < secNo:
        attempts += 1
        print("Try guessing a higher number")
    else:
        attempts +=1
        print(f"Try guessing lower number")
if attempts == maxattempts:
    print(f"All your attempts are over, the number was {secNo}")
