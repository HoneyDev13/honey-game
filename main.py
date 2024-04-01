import random

class Bee:
    def __init__(self):
        self.pollen = 0
        self.honey = 0

    def collect_pollen(self, amount):
        self.pollen += amount

    def make_honey(self):
        if self.pollen >= 10:
            self.honey += 1
            self.pollen -= 10

class Game:
    def __init__(self):
        self.bee = Bee()
        self.levels = 10
        self.enemies = ['spider', 'wasp', 'human']

    def encounter_enemy(self):
        enemy = random.choice(self.enemies)
        print(f"Oh no, a {enemy} is approaching!")
        action = input("Do you want to 'fight' or 'run'? ")
        if action == 'fight':
            if random.randint(0, 1) == 0:
                print(f"You fought off the {enemy} and collected extra pollen!")
                self.bee.collect_pollen(20)
            else:
                print(f"The {enemy} was too strong. You lost some pollen.")
                self.bee.pollen = max(0, self.bee.pollen - 10)
        else:
            print(f"You managed to escape from the {enemy}.")

    def start(self):
        for level in range(1, self.levels + 1):
            print(f"\nStarting level {level}")
            pollen_in_level = level * 10
            self.bee.collect_pollen(pollen_in_level)
            print(f"You collected {pollen_in_level} pollen.")
            self.bee.make_honey()
            print(f"You made honey. Total honey: {self.bee.honey}")
            if random.randint(0, 1) == 0:
                self.encounter_enemy()
            print(f"Finished level {level}. Total pollen: {self.bee.pollen}, Total honey: {self.bee.honey}")

game = Game()
game.start()
