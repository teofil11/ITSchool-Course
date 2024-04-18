import requests
import smtplib, ssl


class Mail:

    def __init__(self):
        self.port = 465
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = "teodorescuteofil@gmail.com"
        self.password = "yepgxnqlvfdgukfq"

    def send(self, emails, subject, content):
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
        service.login(self.sender_mail, self.password)
        
        
        result = service.sendmail(self.sender_mail, emails, f"Subject: {subject}\n\n{content}")

        service.quit()


def send_email(mails,subject,content):
    """
    Send an email to the specified recipients.

    Args:
        mails (str or list): The email address or a list of email addresses to send the email to.
        subject (str): The subject of the email.
        content (str): The content or body of the email.

    """
    mail = Mail()
    mail.send(mails, subject, content)


def get_location():
    url = 'http://ip-api.com/json/'
    response = requests.get(url)
    data = response.json()
    coordinates = {}
    coordinates['lat'] = data['lat']
    coordinates['lon'] = data['lon']
    return coordinates


def get_wether(lat,lon):
    temp = []
    url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m&forecast_days=3&timezone=auto'
    response = requests.get(url)
    data = response.json()
    times = data['hourly']['time']
    temperatures = data['hourly']['temperature_2m']
    for i in range(len(times)):
        temp.append({times[i]:temperatures[i]})
        
    return temp



def email():
    location = get_location()
    temps = get_wether(location['lat'],location['lon'])
    send_email('teodorescu_teofil@yahoo.com', 'wether', temps)
