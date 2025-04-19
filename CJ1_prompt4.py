class Cat:
    def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
        self.arm_length = arm_length       
        self.leg_length = leg_length       
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry

    def describe(self):
        print("Physical Characteristics of the Cat:")
        print(f"Arm Length: {self.arm_length} cm")
        print(f"Leg Length: {self.leg_length} cm")
        print(f"Number of Eyes: {self.num_eyes}")
        print(f"Has Tail: {'Yes' if self.has_tail else 'No'}")
        print(f"Is Furry: {'Yes' if self.is_furry else 'No'}")

my_cat = Cat(arm_length=25.0, leg_length=30.0, num_eyes=2, has_tail=True, is_furry=True)

my_cat.describe()
