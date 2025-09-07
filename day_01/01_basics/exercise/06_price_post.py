# Price notification template
price_notification = "The price of {} is ${}."

# TODO: Post: Latte ($3.5)
c1 = "Latte"
p1 = "3.5"
price_notification1 = price_notification.format(c1, p1)
print(price_notification1)

# TODO: Post: Espresso ($2.75)
c2 = "Espresso"
p2 = "2.75"
price_notification2 = price_notification.format(c2, p2)
print(price_notification2)

# TODO: Post: Cappuccino ($4.0)
c3 = "Capuccino"
p3 = "4.0"
price_notification3 = price_notification.format(c3, p3)
print(price_notification3)