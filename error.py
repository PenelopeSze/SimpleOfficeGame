from work import Work

class Error(Work):
    def __init__(self, health, min_attack, max_attack):
        super().__init__("An Error", health, min_attack, max_attack)

    # Polymorphism
    def attack(self, attack_type, amount_damage):
        if attack_type == "Colleague Advice":
            print("Your colleague is as clueless as you :(")
            return

        super().attack(attack_type, amount_damage)
