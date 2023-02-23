import csv

with open('items.csv', 'r', encoding='windows-1251') as f:
    data = csv.reader(f)
    for i in data:
        print(','.join(i))
