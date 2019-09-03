import random
# get input from console
player = int(input("please enter your number(1/2/3):"))

# generate computer's number

computer = random.randint(1, 3)

print("player's number is %d and computer's number is %d" % (player, computer))

# check result

if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
    print("player win")
elif player == computer:
    print("end in a draw")
else:
    print("computer win")
