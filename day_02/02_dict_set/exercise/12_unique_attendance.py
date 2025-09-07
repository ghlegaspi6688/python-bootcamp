attendee_names = set()

attendee_count = int(input("Attendee count: "))

# TODO: For every attendee expected:
#attendee_name = input("Attendee name: ")
# TODO: Add attendee_name to attendee_names

#print(attendee_names)

att = 0
while att < attendee_count:
    attendee = input("Attendee Name: ")
    attendee_names.add(attendee)
    att = att + 1

print(attendee_names)