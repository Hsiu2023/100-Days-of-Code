print("Welcome to the tip calculator! \n")
bill=float(input("What was the total bill? $\n"))
tip=float(input("How much tip would you like to give? 10,12, or 15? \n"))
people=int(input("How many people to split the bill? \n"))

all_tip=(bill*(tip/100))
all_bill=bill+all_tip
pay=all_bill/people

final="{:.2f}".format(pay)

print(f"Each person should pay: ${final}")
