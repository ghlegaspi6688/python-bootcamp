attendee_names = []

attendee_count = int(input("Attendee count: "))

# TODO: For every attendee expected:
#attendee_name = input("Attendee name: ")
# TODO: Add attendee_name to attendee_names

# TODO: Remove your name in attendees (if it’s there)

# TODO: Remove and print the late attendee (last attendee)

pop = 0 #number of registered attendee, counter
while attendee_count > pop:
    attendee_name = input("Attendee name: ")
    attendee_names.append(attendee_name)
    pop = pop + 1

print(attendee_names)

attendee_name2 = input("Attendee to cancel: ")
attendee_names.remove(attendee_name2)
print(attendee_names)