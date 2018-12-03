import os
import csv

bank_path = os.path.join('Resources', 'budget_data.csv')

#create a file for the financial summary
##financial_analysis_summary = open('financial_analysis.txt', 'a').close()
    
with open(bank_path, 'r', newline='') as bank_file:
    bank_file = csv.reader(bank_file, delimiter=',')
    
    file_header = next(bank_file)
    
    monthly_data = []
    
    for row in bank_file:
        monthly_data.append(row)
    
    total_months = len(monthly_data)
    net_profit = 0
    average_change = 0.00
    greatest_inc = 0 
    greatest_dec = 0
    
    
    
    for each in monthly_data:
        current_profit = int(each[1])
        if current_profit > int(greatest_inc):
            greatest_inc_month = each[0]
            greatest_inc = current_profit
        elif current_profit < int(greatest_dec):
            greatest_dec_month = each[0]
            greatest_dec = current_profit
        
    for each in monthly_data:
        net_profit += int(each[1])
        
    
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print(f'Total Months: {total_months}')
    print(f'Total: $ {net_profit}')
    print(f'Average change: $ {average_change}')
    print(f'Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc})')
    print(f'Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec})')
    
    
    
    
