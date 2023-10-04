from datetime import datetime 

user_input = "15th April, 2023"
date_format = datetime.strptime(user_input, "%dth %B, %Y")

output = date_format.strftime("%Y-%m-%d") 

print(f"The Formatted Date : {output}")