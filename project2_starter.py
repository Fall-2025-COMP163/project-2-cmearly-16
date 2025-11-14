# Project 2
# Christopher Early
# AI assisted in debugging inheritance and proper use of super()

class Character:
    def __init__(self, name, health, strength, magic):
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic
        self.weapon = None

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def attack(self, target):
        damage = self.strength
        if self.weapon:
            damage += self.weapon.damage_bonus
        target.take_damage(damage)

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)

    def display_stats(self):
        print(f"--- {self.name}'s Stats ---")
        print(f"Health: {self.health}")
        print(f"Strength: {self.strength}")
        print(f"Magic: {self.magic}")
        if self.weapon:
            print(f"Weapon: {self.weapon.name} (+{self.weapon.damage_bonus} dmg)")


class Player(Character):
    def __init__(self, name, character_class, health, strength, magic):
        super().__init__(name, health, strength, magic)
        self.character_class = character_class
        self.level = 1
        self.experience = 0

    def display_stats(self):
        super().display_stats()
        print(f"Class: {self.character_class}")
        print(f"Level: {self.level}")
        print(f"Experience: {self.experience}")


class Warrior(Player):
    def __init__(self, name):
        super().__init__(name, "Warrior", health=120, strength=15, magic=5)

    def attack(self, target):
        damage = self.strength
        if self.weapon:
            damage += self.weapon.damage_bonus
        target.take_damage(damage)

    def power_strike(self, target):
        damage = self.strength * 2
        if self.weapon:
            damage += self.weapon.damage_bonus
        target.take_damage(damage)


class Mage(Player):
    def __init__(self, name):
        super().__init__(name, "Mage", health=80, strength=5, magic=20)

    def attack(self, target):
        damage = self.magic // 2
        target.take_damage(damage)

    def fireball(self, target):
        damage = self.magic * 2
        target.take_damage(damage)


class Rogue(Player):
    def __init__(self, name):
        super().__init__(name, "Rogue", health=90, strength=10, magic=10)

    def attack(self, target):
        damage = self.strength
        target.take_damage(damage)

    def sneak_attack(self, target):
        damage = self.strength * 3
        target.take_damage(damage)


class Paladin(Player):
    def __init__(self, name):
        super().__init__(name, "Paladin", health=110, strength=13, magic=12)

    def attack(self, target):
        damage = self.strength + (self.magic // 4)
        if self.weapon:
            damage += self.weapon.damage_bonus
        target.take_damage(damage)

    def holy_smite(self, target):
        damage = (self.strength + self.magic) * 2
        target.take_damage(damage)


class Weapon:
    def __init__(self, name, damage_bonus):
        self.name = name
        self.damage_bonus = damage_bonus

    def display_info(self):
        print(f"Weapon: {self.name} | Damage Bonus: {self.damage_bonus}")
