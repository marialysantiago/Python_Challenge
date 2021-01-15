import csv
filename='Resources/budget_data.csv'
with open(filename) as mydata:
    reader=csv.reader(mydata)
    header=next(reader)
    first_row=next(reader)
    last_month=first_row[1]
    row_count=0
    totalprofit=0
    largestprofit=0
    totalchange=0
    minprofit=0
    last_month_value=int(first_row[1])
  
    for row in reader:
        row_count+=1
        totalprofit+=(int(row[1]))
        last_month_value+=int(row[1])
        monthlychange=int(row[1])-last_month_value
        totalchange+=monthlychange

print(f"Total Months: {row_count}")



