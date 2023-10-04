import csv 

user_input = "people.csv"
with open(user_input, 'r', newline ='') as myfile:
    reader = csv.reader(myfile)
    out = list(reader) 
out.reverse()

output = "output.csv"
with open(output, 'w', newline='') as myfile:
    writer = csv.writer(myfile)
    writer.writerows(out) 

# The output is stored in output.csv file