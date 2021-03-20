#CIS 335 HW 3
#Monica Klosin
#3/18/2021



import csv

with open('diamonds.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#row 1 = carat
#row5 = depth
#row 6 = table


#For Zscore scaling, we found that carat, depth, table were top 3 vars
