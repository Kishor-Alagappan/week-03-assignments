import PyPDF2 

user_input = "part_1.pdf" 
with open(user_input, 'rb') as myfile:
    reader = PyPDF2.PdfReader(myfile) 
    extract = ""
    for num in range(len(reader.pages)):
        page = reader.pages[num]
        text = page.extract_text()
        extract += text 

output = "extracted.txt"
with open(output, 'w', encoding = "utf-8") as myfile:
    myfile.write(text)