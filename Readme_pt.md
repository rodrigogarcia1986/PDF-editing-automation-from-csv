# Script de Automação de E-mail

Este é um script em Python projetado para automatizar o processo de envio de arquivos PDF personalizados para uma lista de destinatários por e-mail. O script lê dados de um arquivo CSV, processa esses dados, gera PDFs personalizados, envia esses PDFs como anexos de e-mail e registra o status dos e-mails enviados em um arquivo JSON.

## Uso

Siga estas etapas para utilizar o script:

### 1. Prepare o Seu Arquivo CSV

Certifique-se de ter um arquivo CSV chamado 'your-csv-file.csv' no mesmo diretório do script. O arquivo CSV deve conter pelo menos três colunas nesta ordem: Nome Completo, CPF (Cadastro de Pessoa Física) e E-mail.

### 2. Crie um Modelo de PDF

Você precisa de um modelo de PDF para sobrepor com os dados personalizados. Crie um arquivo de modelo de PDF chamado 'your-template.pdf' e coloque-o no mesmo diretório do script. O script preencherá este modelo com as informações do destinatário.

### 3. Configure o Servidor SMTP e Credenciais

Forneça os detalhes necessários do servidor SMTP, como o endereço do servidor, a porta, o nome de usuário e a senha no script. Substitua os espaços reservados pelas informações do seu servidor SMTP.

```python
smtp_server = 'smtp.seuservidor.net'
smtp_port = 587  # Normalmente, 587 para TLS
smtp_username = 'nome de usuário'
smtp_password = 'suaSenha'
```


### 4. Personalize o Posicionamento no PDF
Você pode personalizar o posicionamento do nome do destinatário nos PDFs gerados. O script inclui declarações condicionais para ajustar a posição no eixo X com base no tamanho do nome do destinatário.

### 5. Execute o Script
Execute o script. Ele lerá dados do arquivo CSV, limpará e formatará os dados, gerará PDFs personalizados e os enviará por e-mail para os destinatários. O script também registrará o status dos e-mails enviados em um arquivo JSON chamado 'log.json'.

### 6. Revise os Resultados
Após executar o script, você encontrará arquivos PDF individuais na pasta './directory/', cada um com o nome do destinatário. O status dos e-mails enviados, incluindo quaisquer erros, será registrado em 'log.json'. O número de e-mails enviados será exibido no console.

Dependências
Certifique-se de instalar as bibliotecas Python necessárias, se ainda não o fez:

```python
PyPDF2
reportlab
smtplib #(parte da biblioteca padrão do Python)
```

Você pode instalar essas bibliotecas usando pip:

```python
pip install PyPDF2 reportlab
```

Observe que você precisa ter um servidor SMTP funcional e credenciais de conta de e-mail válidas para enviar e-mails usando este script.

### Sinta-se à vontade para modificar o script conforme necessário e adaptá-lo ao seu caso de uso específico.
