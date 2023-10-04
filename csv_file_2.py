import csv 

user_input = "cars_data.txt"
with open(user_input, 'r', newline='') as myfile:
    reader = csv.reader(myfile, delimiter = '|')
    out = list(reader) 
head = out[0]
out = out[1:] 

output = "formatted.csv" 
with open(output,'w', newline='') as myfile:
    writer = csv.writer(myfile, delimiter = ',')
    writer.writerow(head)
    writer.writerows(out)