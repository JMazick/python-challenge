import csv
import os

# Path to collect data from the Resources folder
os.chdir("C:\\Users\\jazly\\OneDrive\\BOOTCAMP\\HOMEWORK\\WEEK-3")

# Define the function and have it accept the 'PyBank' as its sole parameter
PyBank = "00_Homework Assignments Instructions & Data_Week3_Instructions_PyBank_Resources_budget_data.csv"

with open(PyBank) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")
    
    #for row in csv_reader: *********need help on this
        #Date = row[0]
        #ProfitLosses = row[1]
        
