attendee_names = []

attendee_count = int(input("Attendee count: "))  #number of attendee that can be accommodated

# TODO: For every attendee expected:
pop = 0 #number of registered attendee, counter
while attendee_count > pop:
    attendee_name = input("Attendee name: ")
    attendee_names.append(attendee_name)
    pop = pop + 1

# TODO: Add attendee_name to attendee_names

print(attendee_names)
