import random
from random import randint

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

class Weapon(Ability):
    def attack(self):
        weapon_attack = randint(self.attack_strength//2, self.attack_strength)
        return weapon_attack

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.abilities = []
        self.armors = []
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0
    def add_kills(self, num_kills):
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        self.deaths += num_deaths

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def add_armor(self, armor):
        self.armors.append(armor)

    def current_health(self):
        return self.current_health

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_attack = 0
        for ability in self.abilities:
            total_attack += ability.attack()
        return total_attack

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self, damage_amt = 0):
        total_block = 0
        for armor in self.armors:
            total_block = armor.block()
        return total_block

    def take_damage(self, damage):
        self.current_health  = self.current_health - damage
        return self.current_health

    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False
    def fight(self, opponent):
        while self.is_alive() == True and opponent.is_alive() == True:
            if len(self.abilities) > 0 or len(opponent.abilities) > 0:
                opponent.take_damage(self.attack())
                self.take_damage(opponent.attack())
                if opponent.is_alive() == False:
                    self.add_kills(1)
                    opponent.add_deaths(1)
                    print(self.name + ' won')
                else:
                    self.add_deaths(1)
                    self.add_kills(1)
                    print(opponent.name + ' won')
            else:
                print("Draw!")
                return False

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []

    def remove_hero(self, name):
        for hero in self.heroes:
            if name == hero.name:
                self.heroes.remove(hero)
        return 0

    def view_all_heroes(self):
       for hero in self.heroes:
            print('{}'.format(hero.name))
    def add_hero(self, hero):
        self.heroes.append(hero)

    def attack(self, other_team):
        while self.heroes_alive() and other_team.heroes_alive() is True:
            first_team = random.choice(self.heroes_alive())
            second_team = random.choice(other_team.heroes_alive())
            first_team.fight(second_team)
    def heroes_alive(self):
        heroes_alive = []
        for hero in self.heroes:
            if hero.is_alive is True:
                heroes_alive.append(hero)
            return heroes_alive
    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.health = hero.starting_health

    def stats(self):
        for hero in self.heroes:
            print("Hero name: " + hero.name)
            print("Kills: " + str(hero.kills))
            print("Deaths: {} \n".format(hero.deaths))
class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None
    #
    # def create_ability(self):
    #     ability = input("()")




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
    team1 = Team("Team1")
    team2 = Team("Team2")
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    hero3 = Hero("Goku")
    hero4 = Hero("Vegeta")

    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero3.add_ability(ability1)
    hero3.add_ability(ability2)
    hero4.add_ability(ability3)
    hero4.add_ability(ability4)

    team1.add_hero(hero1)
    team1.add_hero(hero2)
    team2.add_hero(hero3)
    team2.add_hero(hero4)
    # print(team2.heroes_alive())

    team1.attack(team2)
