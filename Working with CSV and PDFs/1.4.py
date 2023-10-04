import PyPDF2 as pdf

with open('part_1.pdf', 'rb') as file_1:
    reader_1 = pdf.PdfReader(file_1)
    
    with open('part_2.pdf', 'rb') as file_2:
        reader_2 = pdf.PdfReader(file_2) 
        writer = pdf.PdfWriter() 

        for num in range(len(reader_1.pages)):
            page = reader_1.pages[num] 
            writer.add_page(page)

        for num in range(len(reader_2.pages)):
            page = reader_2.pages[num]
            writer.add_page(page) 
        
        with open('combined.pdf', 'wb') as out_file:
            writer.write(out_file)

