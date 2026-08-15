import imaplib
import email
from email.header import decode_header

# connect to the gmail imap server via ssl
mail=imaplib.IMAP4_SSL("imap.gmail.com")

# login to gmail with email address and application password
mail.login("user", "pass")

# navigate to gmail inbox
mail.select("inbox")

# keywords to search for within the inbox
keywords = ["zoom interview", "teams interview", "in person interview", "in-person interview",
            "call interview", "phone interview"]

# loop through each keyword and search for emails containing that keyword, then flag those emails
for keyword in keywords:
    status, messages = mail.search(None, 'X-GM-RAW', f'"{keyword}"')

    if status == "OK":
        for num in messages[0].split():
            mail.store(num, "+FLAGS", "\\Flagged")

# close the connection and logout from the gmail server
mail.logout()