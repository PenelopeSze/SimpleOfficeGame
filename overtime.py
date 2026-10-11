from work import Work

class Overtime(Work):
    def __init__(self, health, min_attack, max_attack):
        super().__init__("Overtime", health, min_attack, max_attack)

    # Polymorphism
    def attack(self, attack_type, amount_damage):
        if attack_type == "AI Assistance":
            print("AI is giving you false information.")
            return

        super().attack(attack_type, amount_damage)
