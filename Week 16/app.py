from flask import Flask,request
import mysql.connector
import smtplib, ssl

app = Flask(__name__)

connect = mysql.connector.connect(host = 'localhost', user = 'root', password = 'root', database = 'curs')
cursor =  connect.cursor()

class Mail:

    def __init__(self):
        self.port = 465
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = "teodorescuteofil@gmail.com"
        self.password = "asmqpmgvqtwznlyu"

    def send(self, emails, subject, content):
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
        service.login(self.sender_mail, self.password)
        
        
        result = service.sendmail(self.sender_mail, emails, f"Subject: {subject}\n\n{content}")

        service.quit()

@app.route("/persoana", methods=['POST'])
def send_message():
    data = request.get_json()
    nume = data['nume']
    email = data['email']
    message = data['message']
    mail = Mail()
    mail.send(email, nume, message)
    return 'Emailul a fost trimis'


@app.route("/persoana/<char>", methods = ['GET'])
def send_mail(char):
    persons = []
    cursor.execute('select * from persoane')
    persoane = cursor.fetchall()
    for person in persoane:
        if person[1][0].lower() == char.lower():
            persons.append(person)
    return persons
if __name__ == '__main__':
    app.run(debug=True)