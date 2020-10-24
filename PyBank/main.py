import csv
import os

# Path to collect data from the Resources folder
os.chdir("C:\\Users\\jazly\\OneDrive\\BOOTCAMP\\HOMEWORK\\WEEK-3")

# Define the function and have it accept the 'PyBank' as its sole parameter
PyBank = "00_Homework Assignments Instructions & Data_Week3_Instructions_PyBank_Resources_budget_data.csv"

# Define lists
Date = []
ProfitLosses = []
ProfitChange = []
bank = [Date],[ProfitChange]


with open(PyBank) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")
    
    for row in csv_reader:
        Date.append(row[0])
        ProfitLosses.append(int(row[1]))
        
# create loop to have net change calculated between each row
    for x in range(len(ProfitLosses) - 1):
        ProfitChange.append(ProfitLosses[x + 1] - ProfitLosses[x])


# get max value
GreatestIncrease = max(ProfitChange)

# get min value
GreatestDecrease = min(ProfitChange)

Average = round((sum(ProfitChange) / (len(ProfitChange))), 2)
        
# get max and min date value
# grab index of min and max value + 1 and print corresponding value in Date list
inc_date = ProfitChange.index(GreatestIncrease)+1
MaxDate = (Date[inc_date])

dec_date = ProfitChange.index(GreatestDecrease)+1
MinDate = (Date[dec_date])


# define values as integers
TotalMonths = len(Date)
TotalProfits = sum(ProfitLosses)


# print analysis to look pretty
print("Financial Analysis")
print("--------------------------------------")
print(f"Total Months:    {TotalMonths}")
print(f"Total:          ${TotalProfits}")
print(f"Average Change: ${Average}")
print(f"Greatest increase in Profits: {MaxDate} (${GreatestIncrease})")
print(f"Greatest decrease in Profits: {MinDate} (${GreatestDecrease})")



