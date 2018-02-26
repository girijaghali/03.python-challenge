import os
import csv
import datetime

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#initiatlize variables for input and output file names
filename = "employee_data2"
boss_input_csv = os.path.join( "Resources", filename+".csv")
boss_output_csv = os.path.join( "Resources", filename+"_cleaned.csv")

emp_ID = []
emp_Name = []
emp_Fname = []
emp_Lname = []
emp_DOB = []
emp_SSN = []
emp_State = []


with open(boss_input_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
         emp_ID.append(row[0])
         emp_Name = row[1].split(" ")
         emp_Fname.append(emp_Name[0])
         emp_Lname.append(emp_Name[1])
         emp_DOB.append(datetime.datetime.strptime(row[2], "%Y-%m-%d").strftime("%d/%m/%Y"))
         #emp_DOB.append(row[2])
         emp_SSN.append("***-**-" + row[3].split("-")[2])
         emp_State.append(us_state_abbrev[row[4]])
         
new_CSV = zip(emp_ID,emp_Fname,emp_Lname,emp_DOB,emp_SSN,emp_State)

with open(boss_output_csv, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])

    # Write in zipped rows
    writer.writerows(new_CSV)
