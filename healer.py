class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def get_details(self):
        print(f"The name of the character is {self.name} and the health is {self.health}")


class Warrior(Character):
    def __init__(self, name, health, attack_power):
         super().__init__(name, health)
         self.attack_power = attack_power

    def get_details(self):
        super().get_details()
        print(f"Attack power: {self.attack_power}")

    def attack(self, charac: Character):
         if charac.health - self.attack_power >= 0:
              charac.health -= self.attack_power
         else:
              charac.health = 0
         



class Healer(Character):
    def __init__(self, name, health, healing_power):
         super().__init__(name, health)
         self.healing_power = healing_power

    def get_details(self):
         super().get_details()
         print(f"Healing power: {self.healing_power}")


    def heal(self, chara: Character):
            if chara.health + self.healing_power < 100:
                 chara.health += self.healing_power
            else:
                 chara.health = 100 
        

figure_w = Warrior("Lampros_W", 10,10)
figure_h = Healer("Maria_H",100,10)

warrior = Warrior("Lampros", 70, 30)
healer = Healer("Maria", 90, 20)


while figure_w.health < 100:
    figure_h.heal(figure_w)

    figure_w.get_details()
    figure_h.get_details()

