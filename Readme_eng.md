# Email Automation Script

This is a Python script designed to automate the process of sending personalized PDF files to a list of recipients via email. The script reads data from a CSV file, processes it, generates PDFs with customized content, sends these PDFs as email attachments, and logs the status of the sent emails in a JSON file.

## Usage

Follow these steps to use the script:

### 1. Prepare Your CSV File

Make sure you have a CSV file named 'your-csv-file.csv' in the same directory as the script. The CSV file should contain at least three columns in this order: Full Name, CPF (Cadastro de Pessoa Física, a Brazilian individual taxpayer registry number), and Email.

### 2. Create a PDF Template

You'll need a PDF template to overlay with personalized content. Create a PDF template file named 'your-template.pdf' and place it in the same directory as the script. The script will populate this template with recipient information.

### 3. Configure SMTP Server and Credentials

Provide the necessary SMTP server details, such as the server address, port, username, and password in the script. Replace the placeholders with your SMTP server information.

```python
smtp_server = 'smtp.yourserver.net'
smtp_port = 587  # Usually 587 for TLS
smtp_username = 'username'
smtp_password = 'yourPassword'
```

### 4. Customize PDF Placement
You can customize the placement of the recipient's name within the generated PDFs. The script includes conditional statements to adjust the X-axis position based on the length of the recipient's name.

### 5. Run the Script
Execute the script. It will read data from the CSV file, clean and format the data, generate personalized PDFs, and send them as email attachments to the recipients. The script will also log the status of the sent emails in a JSON file named 'log.json.'

### 6. Review the Results
After running the script, you'll find individual PDF files in the './directory/' folder, each named after the recipient. The status of sent emails, including any errors, will be logged in 'log.json.' The number of sent emails will be displayed in the console.

Dependencies
Ensure you have the necessary Python libraries installed, if you haven't already:

```python
PyPDF2
reportlab
smtplib (part of Python's standard library)
You can install these libraries using pip:
```

```python
pip install PyPDF2 reportlab
```

Please note that you need a functioning SMTP server and valid email account credentials to send emails using this script.

Feel free to modify the script as needed and adapt it to your specific use case.
