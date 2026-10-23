from Calories import Calories

#takes inputs and checks the types and ranges are correct
while True:
    try:
        days = int(input("Enter amount of Days 1-7: "))
        if days in range(1,8):
            break
        else:
            raise ValueError
    except ValueError:
        print("Input number between 1 and 7")

while True:
        unit = input("Enter prefered unit type kg | lb: ")
        if unit == "kg" or unit == "lb":
            break
        else:
            print("Enter kg or lb")

while True:
    try:
        weight = int(input("Enter Bodyweight: "))
        if weight in range(10, 1000):
            break
        else:
            print("Weight out of range")
    except ValueError:
        print("Enter Integer")

while True:
    try:
        activeKcal = int(input(f"Enter Average Active Kcal for {days} days: "))
        if activeKcal in range(1, 20000):
            break
        else:
            print("Kcal out of range")
    except ValueError:
        print("Enter Integer")

while True:
    try:
        restKcal = int(input(f"Enter Average Resting Kcal for {days} days: "))
        if restKcal in range(1, 5000):
            break
        else:
            print("Kcal out of range")
    except ValueError:
        print("Enter Integer")

while True:
    try:
        intake = int(input(f"Enter Average Kcal intake for {days} days: "))
        if intake in range(0, 20000):
            break
        else:
            print("Kcal out of range")
    except ValueError:
        print("Enter Integer")



calories = Calories(days, unit, weight, activeKcal, restKcal, intake)

calories.LoseGain()
