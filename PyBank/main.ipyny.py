# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 11:42:39 2021

@author: Margee
"""

# import csv file
import csv

# create path to budget data csv file
filepath = "C:/Users/Margee/python-homework/PyBank/budget_data.csv"

# initialize variables

months = 0
net_profit = 0
net_change = 0
net_change_list = []
month_of_change = []
avg_change= 0.0
greatest_inc = 0
greatest_dec = 0
greatest_date = ""
greatest_dec_date = ""


# open the file in "read" mode ('r') and store the contents in the variable "csvfile"
with open(filepath, 'r') as csvfile:
    # store all of the text from the file inside a variable called "csvreader"
    # print the contents of the csvreader file
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    row = next(csvreader)
    months =  months+1
    profit_loss = int(row[1])
    net_profit = net_profit+profit_loss
    prev_next = int(row[1])
    
    for row in csvreader:
    # calculate the number of months included in the dataset
        profit_loss = int(row[1])
        months = months + 1
             
   
    # Calculate net profit over entire period
        profit_loss = int(row[1])
        net_profit = net_profit + profit_loss                  
                 
    # calculate the average change in profit/losses over the entire period
        net_change = int(row[1]) - prev_next
        prev_next = int(row[1])
        net_change_list = net_change_list + [net_change] 
        month_of_change = month_of_change + [row[0]]
             
    # calculate the greatest increase in profits (date and amount) over the entire period
        if net_change > greatest_inc:
            greatest_inc = net_change
            greatest_date =  row[0]
        
    # calculate the greatest decrease in profits (date and amount) over teh entire period
        if net_change < greatest_dec:
            greatest_dec = net_change
            greatest_dec_date = row[0]
            

    avg_change = round((sum(net_change_list)/len(net_change_list)),2) 
    
    print(f"Financial Analysis")
    print(f"---------------------")
    print(f"Total Months: " + str(months))
    print(f"Total: ${net_profit}")
    print(f"Average Change: ${avg_change}")
    print(f"Greatest Increase in Proifts: {greatest_date} ${greatest_inc}")
    print(f"Greatest Decrease in Profits: {greatest_dec_date} ${greatest_dec}")
    
# Set the output path

output_path = "C:/Users/Margee/python-homework/PyBank/main.txt"

# Open the Output Path as a text
with open(output_path, 'w') as text:
    text.write(f"Financial Analysis\n")
    text.write(f"----------------------\n")
    text.write(f"Total Months: " + str(months) + "\n")
    text.write(f"Total: ${net_profit} + \n")
    text.write(f"Average Change: ${avg_change} = \n")
    text.write(f"Greatest Increase in Proifts: {greatest_date} ${greatest_inc} + \n")
    text.write(f"Greatest Decrease in Profits: {greatest_dec_date} ${greatest_dec}")
    
    
    
    
   
    
   
    
   
