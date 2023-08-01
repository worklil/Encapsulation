import random

suspects = ["Miss Scarlet", "Prof Plum", "Rev Green", "Coloner Mustard", "Mrs Peacock", "Mrs White"]
rooms = ["Kitchen", "Ballroom", "Conservatory", "Diving Room", "Billiard Room", "Library", "Lounge", "Hall", "Study"]
weapons = ["Candlestick", "Daggeer", "Lead Pipe", "Revolver", "Rope", "Spanner"]


class guilty:
    def __init__(self):
        self.__murderer = random.choice(suspects)
        self.__scene_of_the_crime = random.choice(rooms)

        self.__murder_weapon = random.choice(weapons)

    def display_answer(self):
        print(self.__murderer, "-", self.__scene_of_the_crime, "-", self.__murder_weapon)
        print()

    def check_solution(self, murderer, scene_of_the_crime, murder_weapon):
        print()
        if (murderer == self.__murderer)\
                and (scene_of_the_crime == self.__scene_of_the_crime)\
                and (murder_weapon == self.__murder_weapon):
            print("Well done, Sherlock, you nailed it.")
        else:
            print("Wrong, you're more sloth than sleuth.")


def am_I_correct():
    print("Who committed the murder?")
    for i in range(6):
        print(i+1, " ..... ", suspects[i])
    murderer_choice = int(input(">>> "))
    murderer = suspects[murderer_choice-1]

    print("Where was the murder committed?")
    for j in range(9):
        print(j+1, " ..... ", rooms[j])
    room_choice = int(input(">>> "))
    scene_of_the_crime = rooms[room_choice-1]

    print("Which weapon was used?")
    for k in range(6):
        print(k+1, " ..... ", weapons[k])
    weapon_choice = int(input(">>>  "))
    murder_weapon = weapons[weapon_choice-1]

    solution.check_solution(murderer, scene_of_the_crime, murder_weapon)

solution = guilty()

solution.display_answer()

am_I_correct()