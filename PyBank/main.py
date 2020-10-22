import csv
import os

# Path to collect data from the Resources folder
os.chdir("C:\\Users\\jazly\\OneDrive\\BOOTCAMP\\HOMEWORK\\WEEK-3")

# Define the function and have it accept the 'PyBank' as its sole parameter
PyBank = "00_Homework Assignments Instructions & Data_Week3_Instructions_PyBank_Resources_budget_data.csv"

Date = []
ProfitLosses = []
ProfitChange= []

with open(PyBank) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")
    
    for row in csv_reader:
        Date.append(row[0])
        ProfitLosses.append(int(row[1]))
        
    for x in range(len(ProfitLosses) - 1):
        ProfitChange.append(ProfitLosses[x + 1] - ProfitLosses[x])
        
        
        
print(Date)

print(len(Date))

print(ProfitLosses)

print(sum(ProfitLosses))

TotalMonths = len(Date)
TotalProfits = sum(ProfitLosses)

print(TotalMonths)
print(TotalProfits)



AverageChange = (sum(ProfitChange) / (len(ProfitChange)))
print(AverageChange)

