import os
import csv


#initiatlize variables for input and output file names
filename = "budget_data_2"
bank_input_csv = os.path.join( "Resources", filename+".csv")
bank_output_csv = os.path.join( "Resources", filename+"_out.txt")

# variable initialization
dates = []
revenue = []
total_months = 0
total_rev_gain = 0
avg_change = 0
greatest_increase = 0 
greatest_decrease = 0
greatest_increase_val = 0 
greatest_decrease_val = 0
row_text = ""


#open input read file
with open(bank_input_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip header record
    next(csvreader, None)
    #loop through the file. 
    for row in csvreader:
        #calcaulate the sum of revenue
        total_rev_gain += int(row[1])
        #calcualte the row count. Assuming one row per month. 
        total_months +=1
        #write the revenue and dates into lists. This will be later used for min, max
        revenue.append(int(row[1]))
        dates.append(row[0])


#calculations
avg_change = total_rev_gain / total_months
greatest_increase = revenue.index(max(revenue))
greatest_decrease = revenue.index(min(revenue))
greatest_increase_dt = dates[greatest_increase]
greatest_increase_val = revenue[greatest_increase]
greatest_decrease_dt = dates[greatest_decrease]
greatest_decrease_val = revenue[greatest_decrease]


#print to screen  
print ("Financial Analysis")
print("----------------------")
print("Total Months: " + str(total_months))       
print("Total Revenue: " + str(total_rev_gain))
print("Average Revenue Chage: " + str(avg_change))
print("Greatest Increase in Revenue : " + str(greatest_increase_dt) + "(" + str(greatest_increase_val) + ")")
print("Greatest Decrease in Revenue : " + str(greatest_decrease_dt) + "(" + str(greatest_decrease_val) + ")")

#write to a text file, one row at a time. 
with open(bank_output_csv, 'w', newline='') as csvfile:
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile)
    
    row_text = "Financial Analysis"
    csvwriter.writerow ([row_text])
    
    row_text = "----------------------"
    csvwriter.writerow ([row_text])

    row_text = "Total Months: " + str(total_months)
    csvwriter.writerow ([row_text])
    
    row_text = "Total Revenue: " + str(total_rev_gain)
    csvwriter.writerow ([row_text])
    
    row_text = "Average Revenue Change: " + str(avg_change)
    csvwriter.writerow ([row_text])
     
    row_text = "Greatest Increase in Revenue : " + str(greatest_increase_dt) + "(" + str(greatest_increase_val) + ")"
    csvwriter.writerow ([row_text])
     
    row_text = "Greatest Decrease in Revenue : " + str(greatest_decrease_dt) + "(" + str(greatest_decrease_val) + ")"
    csvwriter.writerow ([row_text])