import random

suspects = ["Miss Scarlet", "Prof Plum", "Rev Green", "Coloner Mustard", "Mrs Peacock", "Mrs White"]
rooms = ["Kitchen", "Ballroom", "Conservatory", "Diving Room", "Billiard Room", "Library", "Lounge", "Hall", "Study"]
weapons = ["Candlestick", "Daggeer", "Lead Pipe", "Revolver", "Rope", "Spanner"]


class guilty:
    def __init__(self):
        self.murderer = random.choice(suspects)
        self.scene_of_the_crime = random.choice(rooms)
        self.murder_weapon = random.choice(weapons)

    def __display_answer(self):
        print("From code in method")
        print(self.murderer, "did it")
        print("in the", self.scene_of_the_crime)
        print("with the", self.murder_weapon)


solution = guilty()
# solution.display_answer()

print("From code in main body")
print(solution.__murderer, "did it")
print("in the", solution.scene_of_the_crime)
print("with the", solution.murder_weapon)