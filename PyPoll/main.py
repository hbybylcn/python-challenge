import os

import csv

csv_path=os.path.join("election_data.csv")

with open (csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)


    candidates = {}

    count=0
    winner=0
    winning_candidate=""
    for row in csvreader:

        
        if row[2] in candidates:

            candidates[row[2]]= candidates[row[2]]+1
        else:
            candidates[row[2]]=1

        count=count+1

print(f"The total vote is {count}")


for candidate, votes in candidates.items():
    print(f"{candidate}: % {int((candidates[candidate]/count)*100)}")

    if votes > winner:
        winner = votes
        winning_candidate = candidate
        

print(f"The winner is {winning_candidate}")
  


outputfile=os.path.join("final_result")

with open(outputfile, "w") as datafile:

    writer=csv.writer(datafile)
    writer.writerow(["Total votes:", count])
    writer.writerow([candidates])
    writer.writerow(["Winner",winning_candidate])


    




