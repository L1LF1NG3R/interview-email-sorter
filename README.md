# interview-email-sorter
a python script that automatically scans emails related to job interviews in gmail (zoom, teams, phone, or in-person interviews) and automatically stars them.

# important notes
use this script at your own risk because it requires that your credentials to be hardcoded.

this script requires 2FA to be enabled to acquire app password. HOWEVER, this code BYPASSES 2FA.

if your app password has been accidentally exposed, please change it at "https://myaccount.google.com/apppasswords".


# purpose of this script
i found that i've missed plenty of emails from recruiters inviting me for an interview.

# what it does
it connects to gmail via imap, and it searches the inbox for emails matching interview-related keywords.

it applies gmail's '\flagged' flag to matches, which shows up as a star in gmail.

# how to use
1. go to https://myaccount.google.com/security and turn on 2-Step Verification if it isn't already on.
2. create a new app password. copy the 16-character code google gives you.
3. enter your email address in "user", and paste the 16-character code on "pass" in main.py, line 9.
4. run the script "python main.py"


