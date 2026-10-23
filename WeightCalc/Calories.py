class Calories:
    def __init__(self, days, unit, weight, active, rest, intake):
        self.days = days
        self.unit = unit
        self.weight = weight
        self.active = active
        self.rest = rest
        self.intake = intake

    def AvgBurnedKcal(self):
        return self.active + self.rest

    def TotalBurnedKcal(self):
        return self.AvgBurnedKcal() * self.days

    def TotalIntake(self):
        return self.intake * self.days

    def WeightChange(self):
        amount = (self.TotalIntake() - self.TotalBurnedKcal()) / 3500
        if self.unit == "lb":
            return amount
        elif self.unit == "kg":
            return amount / 2.20462

    def Bodyfat(self):
        return (self.WeightChange() / self.weight) * 100

    def LoseGain(self):
        if self.WeightChange() > 0:
            print(f"\nFor these {self.days} days you have a estimated gain of {round(self.WeightChange(), 2)}{self.unit}, {round(self.Bodyfat(), 2)}% bf")
        elif self.WeightChange() < 0:
            print(f"\nFor these {self.days} days you have a estimated loss of {round(self.WeightChange()*-1, 2)}{self.unit}, {round(self.Bodyfat()*-1, 2)}% bf")
        else:
            print("\nNo change in weight")