min_investment =  0
max_investment = 50000
min_rate = 0
max_rate = 15

#loop to get input for the investment amount and make sure it's between min & max investment amounts
while (investment_amount := int(input(f"Input monthly investment amount (between {min_investment} and {max_investment}): "))) not in range(min_investment + 1, max_investment):
    print(f"--Please input an amount between {min_investment} and {max_investment}--")

#loop to get input for the interest rate and make sure it's between min & max rate amounts
while (interest_rate := int(input(f"Input interest rate to be used (between {min_rate} and {max_rate}): "))) not in range(min_rate + 1, max_rate):
    print(f"--Please input an amount between {min_rate} and {max_rate}--")
        
#loop to input for the duration to calculate for in years and make sure it's greater than zero
while (duration := int(input("Input investment duration [in years] to be used (greater than 0): "))) <= 0:
    print("--Please input an amount greater than 0--")
        
total_months = duration * 12
monthly_rate = 1 + (interest_rate / 1200)
total = 0

#calculates the interest accruement and prints the total per full year calculated
for month in range(1, total_months + 1):
    total += investment_amount
    total = round((total * monthly_rate),2)
    if month % 12 == 0:
        print(f"Year {int(month/12)}: ${total}")

print('\n' + f"Investment Duration: {duration} years\n"
      f"Yearly Interest Rate: {interest_rate}.0%\n"
      f"Monthly Investment Amount: ${investment_amount}\n"
      f"Total Amount of Investment After Compounding: ${total}")
        
print('\n' + "Completed by, Jeremiah Vela")
