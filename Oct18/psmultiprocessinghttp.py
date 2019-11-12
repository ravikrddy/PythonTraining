from smtplib import SMTP
from email.mime.text import MIMEText
import multiprocessing
import requests

smtp_server_address = 'mail.citrite.net'
#smtp_server_address = 'smtp.gmail.com'
#smtp_server_address = 'localhost'


def send_alert_mail(from_addr, to_addr, subject, message):
    mesg = MIMEText(message)
    mesg['From'] = from_addr
    mesg['To'] = to_addr
    mesg['Subject'] = subject

    smtp = SMTP(smtp_server_address)
    smtp.debuglevel = 1
    smtp.sendmail(from_addr, to_addr, mesg.as_string())
    smtp.close()


def web_crawler(url):
    try:
        p_name = multiprocessing.current_process().name
        response = requests.get(url)
        print(f'{p_name}: {url}: {response.content[:128]}')
    except requests.exceptions.ConnectionError as error:
        subject = f'failed request: {p_name}: {url}'
        send_alert_mail('donotreply@pytraining.org', 'ravikumar.chundi@citrix.com', subject, str(error))
        #send_alert_mail('donotreply@pytraining.org', 'ravikrddy@gmail.com', subject, str(error))
        #send_alert_mail('ravi-mac@localhost', 'ravi-mac@localhost', subject, str(error))


def main():
    urls = ['http://linux.org', 'http://kernel.org', 'http://python.org', 'http://golang.org', 'http://perllang.org']

    for url in urls:
        multiprocessing.Process(target=web_crawler, args=(url,)).start()

    for child in multiprocessing.active_children():
        child.join()


if __name__ == '__main__':
    main()
