import os
import csv
import operator

poll_file_path = os.path.join('Resources', 'election_data.csv')
poll_output = open('poll_results.txt', 'w').close()
poll_output_path = os.path.join('poll_results.txt')

    
    
with open(poll_file_path, "r", newline='') as poll_file:
    poll_file = csv.reader(poll_file, delimiter=',')
    file_header = next(poll_file)
    
    poll_data = []
    candidates = []
    
    for row in poll_file:
        poll_data.append(row)
        candidates.append(row[2])

    #finds names of unique candidates that received votes    
    unique_candidates = set(candidates)
    correy_votes = 0
    otooley_votes = 0
    khan_votes = 0
    li_votes = 0
    total_votes = len(poll_data)

    #Calculate each candidates # of votes
    for vote in candidates:
        if vote == "Correy":
            correy_votes +=1
        elif vote == "O'Tooley":
            otooley_votes+=1
        elif vote == "Khan":
            khan_votes+=1
        elif vote == "Li":
            li_votes += 1


    percent_correy= 0
    percent_otooley = 0
    percent_khan = 0
    percent_li = 0

#calculate vote percentages for each candidate
    percent_correy = (correy_votes / total_votes)
    percent_otooley = (otooley_votes / total_votes)
    percent_khan = (khan_votes / total_votes)
    percent_li = (li_votes / total_votes)    
#format vote percentages to 3 decimal places
    percent_correy = "{:.3%}".format(percent_correy)
    percent_otooley ="{:.3%}".format(percent_otooley)
    percent_khan = "{:.3%}".format(percent_khan)
    percent_li = "{:.3%}".format(percent_li)


    #create a dictionary with each unique_candidate set as a key
    #set each key values as a list of ['percentage of votes candidate won', 'total number 
    #of votes each candidate won']
    #ie. {candidate: ['percent of votes won', 'total number of votes won']}
    
    each_candidate_results = {
        "O'Tooley": [percent_otooley, otooley_votes],
        "Correy": [percent_correy, correy_votes],
        "Khan": [percent_khan, khan_votes],
        "Li": [percent_li, li_votes]
    }
    
    sorted_candidate_results={}
    sorting = []
    prev = 0
    current = 0

    for each in each_candidate_results:
        sorting.append(each_candidate_results[each][1])
    
    #sort by highest number of votes
    sorting.sort(reverse = True)


    #for loop to search for candidates in the order of highest votes
    for vote in sorting:
        for candidate in each_candidate_results:
            if vote in each_candidate_results[candidate]:
                sorted_candidate_results.update({candidate: each_candidate_results[candidate]})
            

    print("Election Results\n")
    print("----------------------------------\n")
    print(f'Total Votes: {total_votes}\n')
    print("----------------------------------\n")
    
    
    #calculate the winner
    winner = ""
    winner_votes = 0

    for candidate in sorted_candidate_results:
        current_candidate = sorted_candidate_results[candidate][1]
        if current_candidate > winner_votes:
            winner_votes = current_candidate
            winner = candidate
        print(f'{candidate}: {sorted_candidate_results[candidate][0]} ({sorted_candidate_results[candidate][1]})')



    
    print("----------------------------------\n")
    print(f'Winner: {winner}')
    print("----------------------------------\n")
    
    with open(poll_output_path, 'w') as poll_results:
        poll_results.write("Election Results\n")
        poll_results.write("----------------------------------\n")
        poll_results.write(f'Total Votes: {total_votes}\n')
        poll_results.write("----------------------------------\n")
        for candidate in sorted_candidate_results:
            poll_results.write(f'{candidate}: {sorted_candidate_results[candidate][0]} ({sorted_candidate_results[candidate][1]})\n')
        poll_results.write("----------------------------------\n")
        poll_results.write(f'Winner: {winner}\n')        
        poll_results.write("----------------------------------\n")
