import os
import csv
import datetime
from dateutil import relativedelta

def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month

bank_input_csv = os.path.join( "Resources", "budget_data_1.csv")
dates = []
date_str=[]
revenue = []
total_months = 0
total_rev_gain = 0
avg_change = 0
greatest_increase = 0 
greatest_decrease = 0
greatest_increase_val = 0 
greatest_decrease_val = 0
i=0



with open(bank_input_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
        total_rev_gain += int(row[1])
        #date_str.append(row[0])
        #dates.append(datetime.datetime.strptime(date_str[i], "%b-%Y"))
        #i+=1
        
        dates.append(datetime.datetime.strptime(row[0], "%b-%Y"))
        revenue.append(int(row[1]))

#print(dates)

min_date = min(d for d in dates)
max_date = max(d for d in dates)  
total_months = diff_month(max_date, min_date)
avg_change = total_rev_gain / total_months
greatest_increase = revenue.index(max(revenue))
greatest_decrease = revenue.index(min(revenue))
greatest_increase_dt = dates[greatest_increase]
greatest_increase_val = revenue[greatest_increase]
greatest_decrease_dt = dates[greatest_decrease]
greatest_decrease_val = revenue[greatest_decrease]

r = relativedelta.relativedelta(max_date, min_date)
print(r.months)
   
print(min_date)
print(max_date) 
print(total_months)        
print(total_rev_gain)
print(avg_change)
print(greatest_increase)
print(greatest_decrease)
print(greatest_increase_dt) 
print(greatest_increase_val)
print(greatest_decrease_dt)
print(greatest_decrease_val)
