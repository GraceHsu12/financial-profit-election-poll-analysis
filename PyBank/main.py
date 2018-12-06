#
#author: Grace Hsu
#Date: 12/5/18 Edits
#

import os
import csv

bank_path = os.path.join('Resources', 'budget_data.csv')

#create a file for the financial summary
financial_analysis_summary = open('financial_analysis.txt', 'w').close()

financial_output_path = os.path.join('financial_analysis.txt')

with open(bank_path, 'r', newline='') as bank_file:
    bank_file = csv.reader(bank_file, delimiter=',')
    
    file_header = next(bank_file)
    
    
    #store monthly data in a list format
    monthly_data = []
    month=[]
    profit=[]

    for row in bank_file:
        monthly_data.append(row)
        month.append(row[0])
        profit.append(row[1])

    total_months = len(month)
    net_profit = 0
    average_change = 0.00
    greatest_inc = 0 
    greatest_dec = 0
    


    #Calculate the average change.
    #list to store changes
    profit_change = []

    previous_month = month[0]
    previous_profit = profit[0]
    
    for each in monthly_data:
        current_month = each[0]
        current_profit = each[1]
        
        if current_month != previous_month:
            profit_change.append(int(current_profit) - int(previous_profit))

    #average all the values in the list profit_change
    #this sum function is not adding correctly.
    # Check the profit_change list if it is accurate
    average_change = sum(profit_change)
    #fix len(profit) and check sum calculation
    
    # average_change = average_change / len(profit)
    print(average_change)
    #create for loop to look in profit_change list to find max and min
   # for each in profit_change:





    for each in profit:
        net_profit += int(each)
        

    
    
    
    
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print(f'Total Months: {total_months}')
    print(f'Total: $ {net_profit}')
    print(f'Average change: $ {average_change}')
    # print(f'Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc})')
    # print(f'Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec})')
   
    with open(financial_output_path, 'w') as financial_output:
        financial_output.write("Financial Analysis\n")
        financial_output.write("-------------------------------------------------------\n")
        financial_output.write(f"Total Months: {total_months}\n")
        financial_output.write(f"Total: ${net_profit}\n")
        financial_output.write(f"Average Change: ${average_change}\n")
        # financial_output.write(f"Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc})\n")
        # financial_output.write(f"Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec})\n")
        
    
    
    
