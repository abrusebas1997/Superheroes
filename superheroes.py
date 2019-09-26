import random

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        full_attack = self.attack_strength
        attack = random.randint(0, full_attack)
        return attack

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block
    def block(self):
        block = random.randint(0, self.max_block)
        return block
class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def current_health(self):
        return self.current_health

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        for ability in self.abilities:
            total_attack = ability.attack()
            return total_attack
    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self, damage_amt):
        for armor in self.armors:
            total_block = armor.block()
            return total_block

    def take_damage(self, damage):
        self.current_health  = self.current_health - damage
        return self.current_health

    def is_alive(self):
        if self.current_health >= 0:
            return True
        else:
            return False
    def fight(self, opponent):
        while self.is_alive() == True and opponent.is_alive() == True:
            if len(self.abilities) > 0 or len(opponent.abilities) > 0:
                opponent.take_damage(self.attack())
                self.take_damage(opponent.attack())
                if opponent.is_alive() == False:
                    print(self.name + ' won')
                else:
                    print(opponent.name + ' won')
            else:
                print("Draw!")
                return False
class Weapon(Ability):
    def attack(self):
        weapon_attack = randint(self.attack_strength//2, self.attack_strength)
        return weapon_attack
class Team(name):
    def __init__(self, name):
        self.name = name
        self.heroes = []

    def remove_hero(self, name):
        self.heroes.pop()

    def view_all_heroes(self):
        index = 0
        for hero in self.heroes:
            print("{}{}".format(self.name, self.heroes))
            index += 1
    def add_hero(self, hero):
        self.heroes.append()





if __name__ == "__main__":
    # ability = Ability("Debbuging Ability", 20)
    # print(ability.name)
    # print(ability.attack())

    # armor = Armor("blockpower", 100)
    # print(armor.name)
    # print(armor.block())

    # my_hero = Hero("Grace Hopper", 200)
    # print(my_hero.name)
    # print(my_hero.current_health)

    # ability = Ability("Great Debugging", 50)
    # hero = Hero("Grace Hopper", 200)
    # hero.add_ability(ability)
    # print(hero.abilities)

    # ability = Ability("Great Debugging", 50)
    # another_ability = Ability("Smarty Pants", 90)
    # hero = Hero("Grace Hopper", 200)
    # hero.add_ability(ability)
    # hero.add_ability(another_ability)
    # print(hero.attack())

    # hero = Hero("Grace Hopper", 200)
    # shield = Armor("Shield", 50)
    # hero.add_armor(shield)
    # hero.take_damage(50)
    # print(hero.current_health)

    # hero = Hero("Grace Hopper", 200)
    # hero.take_damage(150)
    # print(hero.is_alive())
    # hero.take_damage(15000)
    # print(hero.is_alive())

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
