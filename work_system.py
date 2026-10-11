from overtime import Overtime
from basic import Basic
from error import Error
from work import Work
import random as r

class WorkSystem:
    def __init__(self):
        self.work_hashmap = {}
        self.player_health = 20
        self.main_menu = """
Please select one of the following
1. Add work
2. List all work
3. Start work :(
Enter your selection (Enter 'exit' to quit): """

        self.attack_menu = """
What do you have in mind?
1. Black Coffee  - Max energy: 10
2. AI Assistant - Max energy: 10
3. Team Work  - Max energy: 15
4. Colleague Advice  - Max energy: 8 
Enter your selection (Enter 'exit' to quit): """

        self.init_work()
        self.run()

    def add_work(self):
        type = input("Enter the type of work: ")
        health = input("Enter the workload: ")
        min_attack = input("Enter the minimum energy needed: ")
        max_attack = input("Enter the maximum energy needed: ")

        new_work = Work(type, health, min_attack, max_attack)
        self.work_hashmap[type] = new_work

    def init_work(self):
        self.work_hashmap["Overtime"] = Overtime(20, 5, 10)
        self.work_hashmap["Basic Work"] = Basic(20, 5, 10)
        self.work_hashmap["An Error"] = Error(20, 5, 10)

    def start_work(self):
        current_work = None
        self.player_health = 20
        while True:
            if current_work == None:
                current_work : Work = r.choice(list(self.work_hashmap.values()))
                print(f"You are assigned {current_work.type.title()}.")
            user_choice = input(self.attack_menu)

            if user_choice == "exit":
                break

            user_choice = int(user_choice)

            damage = r.randint(1, 11)

            if user_choice == 1:
                current_work.attack("Black Coffee", damage)
            elif user_choice == 2:
                current_work.attack("AI Assistant", damage)
            elif user_choice == 3:
                    current_work.attack("Team Work", damage)
            elif user_choice == 4:
                current_work.attack("Colleague Advice", damage)

            if current_work.health <= 0:
                print("You have finished your work.")
                continue

            # if the user dies
            damage_work = r.randint(current_work.min_attack, current_work.max_attack)

            self.player_health = self.player_health - damage_work
            print(f"The {current_work.type} took away {damage_work} of your energy, you have {self.player_health} energy left.")

            if self.player_health <= 0:
                print(f"You died from overwork.")
                break

    def run(self):
        while True:
                user_choice = input(self.main_menu)

                if user_choice == "exit":
                    break

                user_choice = int(user_choice)

                if user_choice == 1:
                    self.add_work()
                if user_choice == 2:
                    self.list_work()
                if user_choice == 3:
                    self.start_work()

    def list_work(self):
        for value in self.work_hashmap.values():
            value : Work = value
            print(value.get_info())

WorkSystem()


