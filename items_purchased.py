import csv
import copy
from statistics import mean

#read csv file customer_purchases
with open('customer_purchases.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    counter = 1
    orders = {}

#create dictionary: keys = customer_id 
#                   value = array of number_of_items
    for line in csv_reader:
        if not line['customer_id'] in orders:
            orders[line['customer_id']] = []
        old_value = orders[line['customer_id']]
        number_of_items = line['number_of_items']
        old_value.append(int(float(number_of_items)))
        orders[line['customer_id']] = old_value

#copy original dictionary into new dictionary
original = orders
average_orders = original.copy()

#create new dictionary to calculate averages
average_purchases = {}
for key in average_orders:
    average = mean(average_orders[key])
    average_purchases[key] = average

#write new csv file with average number of items purchased per customer
with open('average_purchases.csv', 'w') as outcsv:
        writer = csv.DictWriter(outcsv, fieldnames = ["customer_id", "average_number_of_items_purchased"])
        writer.writeheader()
        w = csv.writer(outcsv)
        w.writerows(average_purchases.items())
