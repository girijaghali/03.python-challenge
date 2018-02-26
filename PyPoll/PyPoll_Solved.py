import os
import csv

filename = "election_data_1"

poll_input_csv = os.path.join( "Resources", filename+".csv")
poll_output_csv = os.path.join( "Resources", filename+"_out.txt")

total_votes = 0 
voted_candidates = {}
votes_percent = 0
max_votes = 0
winner = ""
row_text = ""

with open(poll_input_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip header record
    next(csvreader, None)
    #loop through the file. 
    for row in csvreader:
        total_votes += 1
        if row[2] in voted_candidates:
            voted_candidates[row[2]] += 1
        else:
            voted_candidates[row[2]] = 1
max_votes = max(voted_candidates.values())
        

with open(poll_output_csv, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    row_text = "Election Results"
    print(row_text)
    csvwriter.writerow ([row_text])
    
    row_text = "-------------------------"
    print(row_text)
    csvwriter.writerow ([row_text])
    
    row_text = "Total Votes: " + str(total_votes)
    print(row_text)
    csvwriter.writerow ([row_text])
    
    row_text = "-------------------------"
    print(row_text)
    csvwriter.writerow ([row_text])
    
    for key, value in voted_candidates.items():
        votes_percent = (value / total_votes) * 100
        row_text = key + ": " + str(votes_percent) + "% (" + str(value) + ")"
        print(row_text)
        csvwriter.writerow ([row_text])
        
        if value == max_votes:
            winner = key
            
    row_text = "-------------------------"
    print(row_text)
    csvwriter.writerow ([row_text])
        
    row_text = "Winner : " + winner
    print(row_text)
    csvwriter.writerow ([row_text])
        
    row_text = "-------------------------"
    print(row_text)
    csvwriter.writerow ([row_text])
        
