class Employee:
    def __init__(self,name, id):
        self.name = name
        self.id = id
        self.tasks = []
        print(f"Employee {self.name} created with id {self.id}")
    def add_task(self, task):
        print(f"Adding task {task} to {self.name}")
        self.tasks.append(task)


employee1 = Employee(name="Richard", id=1234)
print("middle part")
employee2 = Employee("Jelly", id=9876)
print(employee1.id)