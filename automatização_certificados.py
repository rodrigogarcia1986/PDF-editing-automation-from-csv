from PyPDF2 import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

#clean the csv file

data = []
with open('./Espiritualidade_ módulo 1.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        line = line.split(",")
        data.append([line[2], line[3]])

data = data[1:]
clean_names = []
clean_cpfs = []

for item in data:
    item[0] = item[0].strip('"').strip()
    names = item[0].split(" ")
    #print(names)   
    temp_names = []
    for name in names:        
        name = name.lower()
        if len(name) > 3:
            name = "{}{}".format(name[0].upper(), name[1:])
            #print(name)
        temp_names.append(name)
        #print(temp_names)
        if len(names) == len(temp_names):
            formatted_names = " ".join(temp_names)
            clean_names.append(formatted_names)
            temp_names = []

for item in data:
    item[1] = item[1].strip('"').strip('')
    item[1] = item[1].replace('"', "")
    item[1] = item[1].replace(" ", "")
    item[1] = item[1].replace(".", "")
    item[1] = item[1].replace(".", "")
    item[1] = item[1].replace("-", "")
    
    temp_nums = []
    for num in item[1]:
        temp_nums.append(num)
        if len(temp_nums) == 11:
            temp_nums.insert(3, '.')
            temp_nums.insert(7, '.')
            temp_nums.insert(11, '-')           
            #print(clean_cpfs)
            #clean_cpfs[0].replace(" ", "")
            temp_nums = []

# print(len(clean_cpfs))
# print(len(clean_names))

clean_data = zip(clean_names, clean_cpfs)

count = 0

for name, cpf in clean_data:
    print(name)
    
for name, cpf in clean_data:
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)

    if len(name) <= 10:
        can.drawString(390, 295, name)

    else:
        can.drawString(350, 295, name)
    
    can.drawString(300, 270, cpf)
    can.save()

    #move to the beginning of the StringIO buffer
    packet.seek(0)

    # create a new PDF with Reportlab
    new_pdf = PdfReader(packet)
    # read your existing PDF
    existing_pdf = PdfReader(open("./Certificado final.pdf", "rb"))
    output = PdfWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.pages[0]
    page.merge_page(new_pdf.pages[0])
    output.add_page(page)
    # finally, write "output" to a real file
    output_stream = open("./certificados/Certificado {}.pdf".format(name), "wb")
    output.write(output_stream)
    output_stream.close()
    count += 1