import random

'''
1 for snake
-1 for water
0 for gun
'''


computer = random.choice([1, -1, 0])


youstr = input("Enter your choice: s -> snake, w -> water, g -> gun: ").lower()
yourDict = {"s": 1, "w": -1, "g": 0}
you = yourDict[youstr]


if (you == 1 and computer == -1) or (you == -1 and computer == 0) or (you == 0 and computer == 1):
    print("You win")
elif you == computer:
    print("It's a tie")
else:
    print("You lose")


reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
print("Computer chose:", reverseDict[computer])
print("You chose:", reverseDict[you])
