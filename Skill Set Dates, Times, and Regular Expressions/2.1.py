from datetime import datetime, timedelta 

user_input = "2023-04-15" 
date_format = datetime.strptime(user_input, "%Y-%m-%d") 

output = date_format + timedelta(days=45) 
output_format = output.strftime("%Y-%m-%d") 

print(f'The new date : {output_format}')