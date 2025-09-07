total = 0
running = True
while running:
    command = input("Provide command: ")

    if command == "add":
        pass  # TODO: Ask for number, add to total, and print
        n1 = int(input("Enter First Number: "))
        n2 = int(input("Enter Second Number: "))
        print(n1 + n2)
    elif command == "sub":
        pass  # TODO: Ask for number, subtract to total, and print
        n1 = int(input("Enter First Number: "))
        n2 = int(input("Enter Second Number: "))
        print(n1 - n2)
    elif command == "exit":
        running = False
