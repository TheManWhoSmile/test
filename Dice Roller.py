#make a dice roller
import random


print("""Hello, this is a dice roller""")
amount_of_dice = ""


while True:
    numbertime = 0
    result = ""

    amount_of_dice = input("Please input the amount of dice you want to roll. (r for random): ")
    if amount_of_dice == "quit":
        print("Exiting Application.")
        break

    if amount_of_dice == "r":
        amount_of_dice = random.randrange(0,501)

    for temp in range(int(amount_of_dice)):
        diceroll = random.randrange(1, 7)
        diceroll = str(diceroll)
        numbertime += 1
        result =  f"""{result}
    Dice Number: {numbertime}, result: {diceroll}."""

    print(result)