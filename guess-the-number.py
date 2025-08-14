import random

n = random.randint(1, 100)
a = -1
guesses = 0

while a != n:
    a = int(input("Guess a number between 1 and 100: "))
    guesses += 1
    
    if a > n:
        print("Too high")
    elif a < n:
        print("Too low")
    else:
        print("🎉 Correct!")

print("You guessed the number in", guesses, "tries")
print("The number was:", n)
