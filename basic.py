from work import Work

class Basic(Work):
    def __init__(self, health, min_attack, max_attack):
        super().__init__("Basic Work", health, min_attack, max_attack)

    # Polymorphism
    def attack(self, attack_type, amount_damage):
        if attack_type == "Black Coffee":
            print("You overdosed on coffee.")
            return

        super().attack(attack_type, amount_damage)
