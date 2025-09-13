class CostTracker:
    def __init__(self):
        self.currentexpense = []
        #self.

    def spend(self):
        expense = int(input("Enter Spending: "))
        self.currentexpense.append(expense)

    def refund(self):
        #expense = int(input("Enter Spending: "))
        self.currentexpense.pop(-1)

    def show(self):
        print(self.currentexpense)

    def mainloop(self):
        running = True
        while running:
            command = input("Command: ")
            if command == "spend":
                self.spend()
            elif command == "refund":
                self.refund()
            elif command == "show":
                self.show()
            elif command == "end":
                running = False
            #elif command == "save":
            #    save(current_expenses)
            #elif command == "load":
            #    current_expenses = load()

tracker = CostTracker()
tracker.mainloop()