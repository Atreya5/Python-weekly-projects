# Step 1:importing required libraries
import csv
import random

# Step 2:reading csv
open_file=open(r"C:\Users\hp\Desktop\python_practice\expense.csv\Week 1Expense Tracker\expense.csv")
read_file=csv.reader(open_file)
expense_data=list(read_file)
open_file.close()
# step 3:excluding header
expense_data=expense_data[1:]
# step 4: creating 4 empty list and appending expense data accordingly
groceries,transport,utilities=[],[],[]

for i in expense_data:
    groceries.append(int(i[1]))
    transport.append(int(i[2]))
    utilities.append(int(i[3]))

# print(groceries)
# print(transport)
# print(utilities)

# Step 5: Defining min,max for each category
groceries_low=min(groceries)
groceries_high=max(groceries)

transport_low=min(transport)
transport_high=max(transport)

utilities_low=min(utilities)
utilities_high=max(utilities)

# print(groceries_low)
# print(groceries_high)
# print(transport_low)
# print(transport_high)
# print(utilities_low)
# print(utilities_high)

# Step 6:Creating budget variables for each category

groceries_budget,transportation_budget,utilities_budget=85,58,45
combined_weekly_budget=groceries_budget+transportation_budget+utilities_budget

# Step 7: initialising total spend
print("---12 Weeks---")
print()
total_spend=0

# Step 8:Weekly category costs

for i in range(1,13):
    grocery_cost=random.randint(groceries_low,groceries_high)
    transport_cost=random.randint(transport_low,transport_high)
    utilities_cost=random.randint(utilities_low,utilities_high)
# Step 9:including emergency in transport cost
    if(random.randint(1,12)==1):
        emergency=random.randint(100,200)
        transport_cost+=emergency
# Step 10:addition of costs
    weekly_total=grocery_cost+transport_cost+utilities_cost
    total_spend+=weekly_total

    week_label="Week "+str(i)
    spend_label="Spend="+str(weekly_total)
# Step 11:Checking weekly budget and weekly total
    if(weekly_total>combined_weekly_budget):
        over_amount=weekly_total-combined_weekly_budget
        status="Over budget by $"+str(over_amount)

    elif(weekly_total<combined_weekly_budget):
        under_amount=combined_weekly_budget-weekly_total
        status="Under budget by $"+str(under_amount)

    else:
        status="Exact on Budget"

    print(week_label+": "+spend_label+" -> "+status)

total_budget=combined_weekly_budget*12

diff=total_budget-total_spend

print()
print("---Final Summary---")
print("Total spend: $"+str(total_spend))
print("Total Budget: $"+str(total_budget))

if(diff>0):
    print("You came ahead by $"+str(diff))

elif(diff<0):
    print("You came behind by $"+str(abs(diff)))

else:
    print("exact")








    