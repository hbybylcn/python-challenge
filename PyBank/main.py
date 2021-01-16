



import os

import csv

csv_path=os.path.join("Resources","budget_data.csv")

with open (csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    total_month=0
    total=0
    price_list=[]
    
    for row in csvreader:
         

         
         total= total+int(row[1])

         total_month +=1

         price_list.append(row[1])


    total_diff=0
    max_profit=0
    min_profit=99999999999
    
    for i in range(len(price_list)-1):

        price_current=int(price_list[i])

        price_next=int(price_list[i+1])


        price_change=price_next-price_current

        
        total_diff=total_diff+ price_change

        if price_change > max_profit:

            max_profit= price_change

        if price_change < min_profit:

            min_profit = price_change
    
avarage_change= float(total_diff)/((total_month-1))

outputfile=os.path.join("final_result")

with open(outputfile, "w") as datafile:

    writer=csv.writer(datafile)
    writer.writerow(["Total Months:", total_month])
    writer.writerow(["Total:",total])
    writer.writerow(["Avarage Change:",avarage_change])
    writer.writerow(["Greatest Increase:", min_profit])
    writer.writerow(["Greatest Decrease:", max_profit])





print("Financial Analysis")
print("----------------------------")

print(f"Total months:  {total_month}")
print(f"Total: {total}")
print(f"Avarage Change : {float(avarage_change)}")
print(f"Greatest Increase in Proffits: {max_profit}")
print(f"Greatest Decrease in Profits : {min_profit}")



