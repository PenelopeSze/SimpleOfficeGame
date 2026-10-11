SimpleOfficeGame

A text-based command-line game written in Python that simulates surviving daily office tasks, workplace errors, and overtime.

Players navigate daily work scenarios by making choices such as drinking coffee, seeking advice from colleagues, or relying on AI assistance while managing limited player energy against incoming work demands.

---

Features & OOP Concepts

- Object Oriented Architecture: Uses inheritance and polymorphism across specialized task classes inheriting from a base `Work` class.
- Specialized Work Classes:
    - `Basic`: Standard office tasks. Be careful when drinking too much Black Coffee!
    - `Error`: Unexpected bugs or errors. Requesting Colleague Advice might reveal they are as clueless as you are!
    - `Overtime`: Late-night workload. Relying on AI Assistance might give you false information!


Menu & Energy System:
- Track player health/energy against random workload damage.
- Add custom tasks dynamically to the system.

---

File Structure

- `work.py`: Base class containing shared workload logic and damage tracking.
- `basic.py`: Subclass handling standard basic tasks and coffee special conditions.
- `error.py`: Subclass managing error tasks and advice handling.
- `overtime.py`: Subclass managing overtime tasks and AI prompt interactions.
- `work_system.py`: Main interactive menu and game loop (`WorkSystem`).

---

How to Run

1. Clone the repository:
```bash
git clone https://github.com/PenelopeSze/SimpleOfficeGame.git
cd SimpleOfficeGame

```


2. Run the game:
```bash
python work_system.py

```

---

How to Play

1. Start the main game loop from `work_system.py`.
2. Choose to Add Work, List All Work, or Start Work.
3. During work execution, choose your action (e.g. Black Coffee, AI Assistant, Team Work, or Colleague Advice) to tackle your assigned workload.
4. Keep an eye on your energy level, if it hits `0`, you die from overwork!
