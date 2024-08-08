# Prompt the user to enter today's day of the week and the number of days after today for a future day
today = int(input("Enter today's day (0 for Sunday, 1 for Monday, ..., 6 for Saturday): "))
days_after_today = int(input("Enter the number of days elapsed since today: "))

# Compute the future day of the week
future_day = (today + days_after_today) % 7

# Display the future day of the week
if future_day == 0:
    print("The future day is Sunday.")
elif future_day == 1:
    print("The future day is Monday.")
elif future_day == 2:
    print("The future day is Tuesday.")
elif future_day == 3:
    print("The future day is Wednesday.")
elif future_day == 4:
    print("The future day is Thursday.")
elif future_day == 5:
    print("The future day is Friday.")
else:
    print("The future day is Saturday.")
