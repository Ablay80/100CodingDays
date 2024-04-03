#TIP calculator
print("Welcome to the tip calculator.\n")
sum = float(input("What was the total bill? Enter summ: $"))
per = int(
    input(
        "What persentage tip would you like to give? 10, 12 or 15?\nEnter summ: "
    ))
ppl = int(input("How many people to split the bill? "))
total_sum = sum + (sum * (per / 100))
pay = round(total_sum / ppl, 2)
print(f"Each person should pay: ${pay}")