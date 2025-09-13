class Employee:
    """Class representation for employee data"""

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.tasks = []
        print(f"Employee {self.name} created with ID {self.id}")

    def add_work(self, task):
        print(f"Added work {task} to {self.name}")
        return self.tasks.append(task)
class Recruiter:
    def __init__(self, name, id, agency):
        super().__init__(name, id)
        self.agency = agency

    def done(self):
        print(f"Recruited 1 person")

class Developer:
    def __init__(self, name, id, develop, module):
        super().__init__(name, id)
        self.develop = develop
        self.module = module

    def done(self):
        print(f"Added work {task} to {self.name}")

class Manager:
    def __init__(self, name, id, proj):
        super().__init__(name, id)
        self.proj = proj

    def done(self):
        print(f"Added work {task} to {self.name}")
