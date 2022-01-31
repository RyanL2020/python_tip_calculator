#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
# divide total_bill_number / guest_split_number * 1.12
# round guest_split_number 2 decimal spaces
print("Welcome to the tip calculator!")

total_bill = input("How much is the bill?")
total_bill_number = int(total_bill)

percent_tip = input("How much tip would you like to give? 10, 12, or 15?")
percent_tip_number = int(percent_tip)

guest_split = input("How many people to split the bill?")
guest_split_number = int(guest_split)

result = (total_bill_number / guest_split_number) * 1.12
result_rounded = round(result, 2)
print(f"Everyone pays: {result_rounded}")
