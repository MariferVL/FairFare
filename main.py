import time

# Asking for total bill
print("🍽️ Welcome to FairFare! Ready to split the bill? Let's make it easy! 🍽️")
time.sleep(1)
total_bill = float(input("💵 What's the grand total of the bill? \n Please include all your delicious indulgences: $"))

# Getting tip percentage and Num of people
tip_percentage = int(input("💰 How generous are we feeling today? \n What percentage would you like to tip our amazing servers? (e.g., 15 for 15%): "))

number_of_people = int(input("👥 How many wonderful friends are we splitting this bill with today? "))

# Simulating calculation
print("🔢 Crunching the numbers...")
time.sleep(2)

# Calculations
tip_amount = (tip_percentage / 100) * total_bill
total_with_tip = total_bill + tip_amount
amount_per_person = total_with_tip / number_of_people

# Display the result
print("🧾 Here's the breakdown:")
time.sleep(1)
print(f"🍲 Total Bill: ${total_bill:.2f}")
print(f"💸 Tip ({tip_percentage}%): ${tip_amount:.2f}")
print(f"🤑 Total with Tip: ${total_with_tip:.2f}")
print(f"💳 Each person should contribute: ${amount_per_person:.2f}")

