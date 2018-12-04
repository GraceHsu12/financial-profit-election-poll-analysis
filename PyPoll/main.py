import os
import csv

poll_file_path = os.path.join('Resources', 'election_data.csv')
poll_results = open('poll_results.txt', 'w').close()

    
    
with open(poll_file_path, "r", newline='') as poll_file:
    poll_file = csv.reader(poll_file, delimiter=',')
    file_header = next(poll_file)
    
    poll_data = []
    voter_ids = []
    county = []
    candidates = []
    
    for row in poll_file:
        poll_data.append(row)
        voter_ids.append(row[0])
        candidates.append(row[2])
        
    #finds names of unique candidates that received votes    
    unique_candidates = set(candidates)
    print(unique_candidates)
    
    #create a dictionary with each unique_candidate set as a key
    #set each key values as a list of ['percentage of votes candidate won', 'total number 
    #of votes each candidate won']
    #ie. {candidate: ['percent of votes won', 'total number of votes won']}
    
    each_candidate_results = {}
    
    
    
    print("Election Results\n")
    print("----------------------------------\n")
    print(f'Total Votes: {len(poll_data)}\n')
    print("----------------------------------\n")
    
    #print the dictionary with each key:value pair as a separate line
    #use a forloop to go through each key:value pair
    #maybe define a function to do this.
    
    
    print("----------------------------------\n")
    #print(f'Winner: {winner}')
    print("----------------------------------\n")
    