import random
from Profession import Profession
from BattleOperator import BattleOperator
from class_list import class_list

print("""Welcome to MINI RPG Game.
You need to create character which will fight against computer.
You have 4 classes to choose.
1. Mage
2. Warrior
3. Archer
4. Paladin
""")

class_choice = input("Type class name to choose class.")
player_nickname = input("Give your character a name.")

computer_class = random.choice(class_list)

battleOperator = BattleOperator()

if class_choice.lower() == "mage":
    mage = Profession(player_nickname, 60, 20, 20)
    print("You have chosen mage.")
    battleOperator.battle(mage, computer_class)
elif class_choice.lower() == "warrior":
    warrior = Profession(player_nickname, 100, 6, 20)
    print("You have chosen warrior.")
    battleOperator.battle(warrior, computer_class)
elif class_choice.lower() == "archer":
    archer = Profession(player_nickname, 70, 13, 20)
    print("You have chosen archer.")
    battleOperator.battle(archer, computer_class)
elif class_choice.lower() == "paladin":
    paladin = Profession(player_nickname, 80, 10, 20)
    print("You have chosen paladin.")
    battleOperator.battle(paladin, computer_class)






