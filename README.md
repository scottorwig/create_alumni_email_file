# create_alumni_email_file
Using a raw text file of emails, a file of current user's emails, and an ignore list of emails, creates a file of alumni users
and puts the addresses in a file so that they can be pasted into the BCC field of a promotional 
email to alumni.

Start with a raw text file of email addresses in a text file called "raw_emails.txt", consisting of email addresses 
from older mailing lists  used for a school team over the years. 
Extracts only valid addresses from the file. 
Those addresses are then compared to two other files, 
(1) "current_members.txt", which consists of current members of the team. Those email addresses are excluded, and
(2) "do_not_email.txt", which will be blank at first, but will be manually populated as people respond not to contact them again.
All emails not excluded are then written to the "alumni_emails.txt" file, each separated by a comma, so that the can be 
manually copied and pasted into the BCC field of a promotional email.
