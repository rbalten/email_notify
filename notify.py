import smtplib
import getpass

def sendEmail(toaddrs, subject, message):
    # setup the from address
    fromaddr = 'notification@notify.py'
    # construct the message
    msg = 'Subject: {}\r\nFrom: {}\r\nTo: {}\r\n\r\n{}'.format(subject, fromaddr, ', '.join(toaddrs), message)

    # send the message
    # NOTE: this requires a local SMTP server to be running
    s = smtplib.SMTP('localhost')
    s.sendmail(fromaddr, toaddrs, msg)
    s.quit()
