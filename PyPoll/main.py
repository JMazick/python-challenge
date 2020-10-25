import csv
import os

# Path to collect date from the Resources folder
os.chdir("C:\\Users\\jazly\\OneDrive\\BOOTCAMP\\HOMEWORK\\WEEK-3")

# Define the function and have it accept the 'PyPoll' as its sole parameter
PyPoll = "00_Homework Assignments Instructions & Data_Week3_Instructions_PyPoll_Resources_election_data.csv"


# Define lists
Voter_ID = []
County = []
Candidate = []


with open(PyPoll) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")
    
    for row in csv_reader:
        Voter_ID.append(int(row[0]))
        County.append(row[1])
        Candidate.append(row[2])
                
    print(Candidate)
        
TotalVotes = len(Voter_ID)
print(TotalVotes)


