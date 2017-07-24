import sys

import argparse 
parser = argparse.ArgumentParser()
parser.add_argument("target")
parser.add_argument("--subject", "-s", default="{}".format(sys.argv[0]))
parser.add_argument("--message", "-m", default=None)
args = parser.parse_args()

if args.message is None:
    args.message = sys.stdin.read()

import smtplib
from email.mime.text import MIMEText
import getpass

msg = MIMEText(args.message)
msg["Subject"] = args.subject
msg["To"] = args.target
msg["From"] = "{} ({})".format(sys.argv[0], getpass.getuser())

s = smtplib.SMTP("localhost")
s.send_message(msg)
s.quit()
