
import imaplib
import email
from email.header import decode_header
import webbrowser
import os
import sys
# username and password of the gmail account

username = ""
password = ""

imap = imaplib.IMAP4_SSL("imap.gmail.com")


result = imap.login(username, password)

imap.select('"[Gmail]/All Mail"',readonly = True)

response, messages = imap.search(None,'UnSeen')
messages = messages[0].split()

latest = int(messages[-1])


oldest = int(messages[0])



original_stdout = sys.stdout


with open('latestUnreadMail.json', 'w') as f:
    sys.stdout = f 
    
    for i in range(latest, latest-1, -1):
        # fetch
        res, msg = imap.fetch(str(i), "(RFC822)")
        
        for response in msg:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])
                jsonContent="{"+'"'+"Date"+'"'+":"+'"'+msg["Date"]+'"'+","+'"'+"From"+'"'+":"+'"'+msg["From"]+'"'+","+'"'+"Subject"+'"'+":"+'"'+msg["Subject"]+'"'+"}\n"
                print(jsonContent)
        for part in msg.walk():
            if part.get_content_type() == "text / plain":
                body = part.get_payload(decode = True)
                print(f'Body: {body.decode("UTF-8")}', )
    sys.stdout = original_stdout 



