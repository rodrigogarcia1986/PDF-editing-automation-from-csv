# Open the the csv file and select the data you need to store it in an empty array
data = []
with open('your-csv-file.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        line = line.split(",")
        data.append([line[2], line[3], line[1]])


# Create arrays for storing the different data (or, if you prefer, use a dictionary from the beggining)
data = data[1:]
clean_names = []
clean_ids = []
clean_emails = []

# A loop for cleaning and formatting

for item in data:
    item[0] = item[0].strip('"').strip()
    names = item[0].split(" ")
    #print(names)   
    temp_names = []
    for name in names:        
        name = name.lower()
        if len(name) >= 3:
            name = "{}{}".format(name[0].upper(), name[1:])
            #print(name)
        temp_names.append(name)    
        #print(temp_names)
        
        if len(names) == len(temp_names):
            formatted_names = " ".join(temp_names)
            clean_names.append(formatted_names)
            temp_names = []
    item[2] = item[2].strip('"')
    clean_emails.append(item[2])

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
            clean_ids.append("".join(temp_nums))
            temp_nums = []

#zip the data in a single variable
clean_data = zip(clean_names, clean_cpfs, clean_emails)

status = [] #an array of dictionaries

for name, id, email in clean_data:
    status.append({'name': name,
     'id': id,
     'e-mail': email,
     'sent': False})

#print(status) 

# Impor libraries
from PyPDF2 import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

#check data

#print(clean_data)
#print(clean_cpfs)
#print(clean_names)
#print(clean_emails)

# set the loop for writing the data
count = 0
    
for name in clean_names:

    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter) #create a canva to overlay the pdf (in the following example, I've checked the names' lenghts in order to  adjust them int the x axis)

    if len(name) <= 10:
        can.drawString(420, 295, name)

    elif len(name) <= 15:
        can.drawString(390, 295, name)
    
    elif len(name) >= 30:
        can.drawString(375, 295, name)

    else:
        can.drawString(350, 295, name)
    
    can.drawString(300, 270, clean_cpfs[count])
    can.save()

    #move to the beginning of the StringIO buffer
    packet.seek(0)

    # create a new PDF with Reportlab
    new_pdf = PdfReader(packet)
    # read your existing PDF-template
    existing_pdf = PdfReader(open("your-template.pdf", "rb"))
    output = PdfWriter()
    # add the "overlay" (which is the new pdf) on the existing page
    page = existing_pdf.pages[0]
    page.merge_page(new_pdf.pages[0])
    output.add_page(page)
    # finally, write "output" to a real file
    output_stream = open("./directory/filename {}.pdf".format(name), "wb")
    output.write(output_stream)
    output_stream.close()
    count += 1   


#import libraries
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import json

# Configurer SMTP server and credentials
smtp_server = 'smtp.yourserver.net'  
smtp_port = 587  #(usually 587 for  TLS)
smtp_username = 'username'  # your api key or username
smtp_password = 'yourPassword'  # your password

count = 1 #a counter for sent emails
#loop for sending emails
for person in status:
    if person['sent'] == False: #check if email has already been sent
        print('Sending file to ' + person['nome'] + " using the email address " + participante['e-mail']) 

    # setting email information
    sender_email = 'the-sender-email'
    recipient_email = person['e-mail']
    subject = 'Sending the pdf you want'
    message_text = f'Hello, {person["nome"]}!\nWe are sending you this pdf.'

    # Create a MIMEMultipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Add message body
    msg.attach(MIMEText(message_text, 'plain'))

    # Attach the file
    file_path = f'./directory/File {person["nome"]}.pdf'  # Use the name you've chosen (in this example, each file will be named after the person's name
    with open(file_path, 'rb') as attachment:
        part = MIMEApplication(attachment.read(), Name=f'File {participante["nome"]}.pdf') #The name you've just chosen above

    # Define the headers
    part['Content-Disposition'] = f'attachment; filename="{file_path}"'
    msg.attach(part)

    # Try connecting SMTP server
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Send e-mail
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print('Email sent!')

    except Exception as e:
        print('Error when sending e-mail:', str(e))
        person['erro': str(e)] #add error to the specific person
    
    person['sent'] = True
    count +=1 #update the counter for sent emails


#Salve the dictionary array with the updated info in a json file
with open('log.json', 'w') as json_file:
# Use json.dump to write the data
    json.dump(status, json_file)

print(f'Data saved in "log.json"')
print("Number of sent emails:", count)

