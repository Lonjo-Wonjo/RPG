#The following Classes will be defined as 'playable charcters'
class playable:
    def __init__(self, name, batk, den, luck):
        self.name = name
        self.batk = batk
        self.den = den
        self.luck = luck

Knight = playable("Knight", 5, 5, 2)
Paladin = playable("Paladin", 3, 7, 3)
Assassin = playable("Assassin", 7, 3, 4)

print(Knight.name, Paladin.name, Assassin.name)
def CharcterSelect():
    Charcter_Spec = input("Choose which charcter you would like to see")
    if Charcter_Spec == "Knight":
        print("A knight in shinning armor, he's a great charcter to choose for beginners.", "His attack is",
              Knight.batk, "and his defense is", Knight.den, ",with luck of", Knight.luck)
        achoice = input("Is this your choice for your character?")
        if achoice == "yes":
            print("Alrighty! Adventure awaits!")
        if achoice == "no":
            print("That's Okay!, choose again.")
            CharcterSelect()
    if Charcter_Spec == "Paladin":
        print("A holy warrior, excellent for more defensive players.", "Their attack is", Paladin.batk,
              "and their defense is", Paladin.den, ",with luck of", Paladin.luck)
        bchoice = input("Is this your choice for your character?")
        if bchoice == "yes":
            print("Alrighty! Adventure awaits!")
        if bchoice == "no":
            print("That's Okay!, choose again.")
            CharcterSelect()
    if Charcter_Spec == "Assassin":
        print("A rouge warrior, more attack at the cost of defense", "Her attack is", Assassin.batk,
              "and her defense is", Assassin.den, ",with luck of", Assassin.luck)
        cchoice = input("Is this your choice for your character?")
        if cchoice == "yes":
            print("Alrighty! Adventure awaits!")
        if cchoice == "no":
            print("That's Okay!, choose again.")
            CharcterSelect()

CharcterSelect()
#The following class defines stats given to the enemy. I hope to be able to implament these enemies into an array.
class enemies:
    def __init__(enemy, name, batk, den, luck):
        enemy.name = name
        enemy.batk = batk
        enemy.den = den
        enemy.luck = luck

Level1Enemies = ["goblin","slime","skeleton"]
Level2Enemies = ["zombie","wrath","revenant"]
Level3Enemies = ["corrupted one","cursed creature","snake-thing"]
#Defining enemy groups now so that each group is defined by the same attributes that the "enemies" class dictates.

Level1Enemies = enemies(["goblin","slime","skeleton"], 2, 1, 1)
Level2Enemies = enemies(["zombie","wrath","revenant"], 3, 3, 2)
Level3Enemies = enemies(["corrupted one","cursed creature","snake-thing"], 4, 5, 3)
#I want to, in a later build coming soon, to sucessfully define the stat attributes and implament a combat system.
#I am unsure whether I want a linear story or it to have a gameplay loop similar to a rougelite.