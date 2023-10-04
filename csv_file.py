import csv 

user_input = "people.csv"
with open(user_input, 'r', newline ='') as file:
    reader = csv.reader(file)
    out = list(reader) 
out.reverse()

output = "output.csv"
with open(output, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(out) 

# The output is stored in output.csv file