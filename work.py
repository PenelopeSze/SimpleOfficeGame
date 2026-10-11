class Work:

    def __init__(self, type, health, min_attack, max_attack):
        self.type = type
        self.health = health
        self.min_attack = min_attack
        self.max_attack = max_attack

    def get_info(self):
        return f"{self.type} needs {self.health} energy to complete. It can deplete your energy by {self.min_attack}-{self.max_attack}"

    def attack(self, attack_type, amount_damage):
        self.health = self.health - amount_damage
        print(f"You tackled {amount_damage}% of your workload from {self.type} and {self.health}% is left.")
