# create_alumni_email_file
This code was developed for use by a high school sports team that uses parent and athelete email
distribution lists. The lists are repopulated each season, but text files remain from each season
of the people on each list. We want to generate a comma-seprated list of emails of 
parents and athletes were are no longer on the team for use in future fundraising.

Using directory of .txt files containing emails, a file of current user's emails, and an ignore list of emails, 
creates a file of alumni emails and puts the addresses in a file so that they can be pasted into 
the BCC field of a promotional  email to alumni.

Start with a directory called "email_files" and put .txt files that contains email addresses from past seasons.
from older mailing lists  used for a school team over the years. 
Extracts only valid addresses from the file. 
Those addresses are then compared to two other files, 
(1) "current_members.txt", which consists of current members of the team. Those email addresses are excluded, and
(2) "do_not_email.txt", which will be blank at first, but will be manually populated as people respond not to contact them again.
All emails not excluded are then written to the "alumni_emails.txt" file, each separated by a comma, so that the can be 
manually copied and pasted into the BCC field of a promotional email.
