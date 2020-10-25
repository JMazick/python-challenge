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
    

    Names = list(set(Candidate))
    namesorder = [3, 1, 2, 0]
    Names = [Names[y] for y in namesorder]
print(Names)


namevotes = {}


Counter = 0

for i in range(len(Names)):
    for x in range(len(Candidate)):
        if Candidate[x] == Names[i]:
            Counter += 1
    print(Counter)
    namevotes[Names[i]] = Counter
    Counter = 0



TotalVotes = len(Voter_ID)
votes = [(namevotes["Khan"]), (namevotes["Correy"]), (namevotes["Li"]), (namevotes["O'Tooley"])]


KhanPercent = round((namevotes["Khan"] / TotalVotes) * 100, 3)
CorreyPercent = round((namevotes["Correy"] / TotalVotes) * 100, 3)
LiPercent = round((namevotes["Li"] / TotalVotes) * 100, 3)
OTooleyPercent = round((namevotes["O'Tooley"] / TotalVotes) * 100, 3)

percents = [KhanPercent, CorreyPercent, LiPercent, OTooleyPercent]
VotePercent = {"Khan": KhanPercent,
               "Correy": CorreyPercent,
               "Li": LiPercent,
               "O'Tooley": OTooleyPercent}
maxpercent = max(percents)


print("Election Results")
print("--------------------------------")
print(f"Total Votes: {TotalVotes}")
print("--------------------------------")
print(f"{Names[0]}: {KhanPercent}% ({votes[0]})")
print(f"{Names[1]}: {CorreyPercent}% ({votes[1]})")
print(f"{Names[2]}: {LiPercent}% ({votes[2]})")
print(f"{Names[3]}: {OTooleyPercent}% ({votes[3]})")
print("--------------------------------")
print(f"Winner: {names[0]}")
