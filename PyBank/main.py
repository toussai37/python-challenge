# Dependencies
import os
import csv


# csv to Load
budget_csv = os.path.join('Resources', 'budget_data.csv')

# lists
months = []
net_total = []
the_changes = []

# Read Files
with open(budget_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:

        months.append(row[0])
        
        net_total.append(int(row[1]))
    
        total_months = len(months)


    for i in range(len(net_total)-1):
        
        the_changes.append(net_total[i+1]-net_total[i])
        
        losses_month = (the_changes.index(min(the_changes)) + 1) 

        profits_month = (the_changes.index(max(the_changes)) + 1)
        
        greatest_decrease_in_losses = min(the_changes)

        greatest_increase_in_profits = max(the_changes)

        

    
# print analysis        
print("Financial Analysis")
print("-----------------------------------------------------------")
print("Total Months: " + str(total_months))
print("Total: " + "$" + str(sum(net_total)))
print("Average Change: " + "$" + (str(round(sum(the_changes)/len(the_changes)))))
print("Greatest Increase in Profits: " + (months[profits_month]) + " ($" + (str(greatest_increase_in_profits)) + ")")
print("Greatest Decrease in Profits: " + (months[losses_month]) + " ($" + (str(greatest_decrease_in_losses)) + ")")

        
output_path = os.path.join("analysis", "analysis.txt")

with open(output_path, 'w') as txtfile:

    txtfile.write("Financial Analysis" + "\n")
    txtfile.write("----------------------------------------------------------" + "\n")
    txtfile.write("Total Months: " + str(total_months) + "\n")
    txtfile.write("Total: " + "$" + str(sum(net_total)) + "\n")
    txtfile.write("Average Change: " + "$" + str(round(sum(the_changes)/len(the_changes))) + "\n")
    txtfile.write("Greatest Increase in Profits: " + (months[profits_month]) + " ($" + (str(greatest_increase_in_profits)) + ")" + "\n")
    txtfile.write("Greatest Decrease in Profits: " + (months[losses_month]) + " ($" + (str(greatest_decrease_in_losses)) + ")")

