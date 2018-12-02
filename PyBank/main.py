import os
import csv

bank_path = os.path.join('..', 'Resources', 'budget_data.csv')

with open(bank_path, 'r+', newline='') as bank_path_file:
    bank_path_file = csv.reader(bank_path_file, delimiter=',')
    
    financial_analysis_summary = open("financial_analysis.txt", "w")
    
    file_header = Next(bank_path_file)
    
    
    
    print("Financial Analysis")
    print("----------------------------------------------------------")
    
    
    
    #is this really needed? I read some forums saying that the 'with open' syntax automatically closes the opened file for you.
    bank_path_file.close()