init python:
    class Character:
        def __init__(self, name, hp, hp_max, attack):
            self.name = name
            self.hp = hp
            self.hp_max = hp_max
            self.attack = attack
            

        def is_alive(self):
            return self.hp > 0

        def take_damage(self, damage):
            self.hp -= damage
            if self.hp < 0:
                self.hp = 0
        
        def heal(self, amount):
            self.hp += amount
            if self.hp > self.hp_max:
                self.hp = self.hp_max

        def attack_character(self, other):
            damage = self.attack 
            other.take_damage(damage)
            return damage

    