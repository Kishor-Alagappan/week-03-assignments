import re

email_regex = r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$'
 
with open("emails.txt", 'r') as my_file:
    emails = my_file.read().splitlines()

valid = [email for email in emails if re.match(email_regex, email)]

print("The valid Emails")
for email in valid:
    print(email)