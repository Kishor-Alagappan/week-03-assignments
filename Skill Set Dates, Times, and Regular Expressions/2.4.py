import re 

with open('patterns.txt', 'r') as my_file:
    text = my_file.read()

date_regex = r'\d{2}/\d{2}/\d{4}|\d{1,2}-\d{2}-\d{4}|\d{2}\.\d{2}\.\d{4}|\d{2}-\d{2}-\d{2}'
dates = re.findall(date_regex, text)

print('Dates in the file:')
for date in dates:
    print(date)