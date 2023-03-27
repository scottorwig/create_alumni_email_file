# create_alumni_email_file
This code was developed for use by a high school sports team that uses parent and athelete email
distribution lists. The lists are repopulated each season, but text files remain from past seasons
of the people on each list. We want to generate a comma-seprated list of emails of 
parents and athletes were are no longer on the team for use in future fundraising.

Using directory of .txt and .csv files containing emails, a directory of current user's emails, 
and an ignore list of emails, this code creates a file of alumni emails 
and puts the addresses in a file so that they can be pasted into 
the BCC field of a promotional  email to alumni.

Start with a directory called "past_member_files" and put into it .txt and .csv files
that contain email addresses from past seasons.
Add a directory called "current_members" and put into it .txt and .csv files
that contain email addresses active this season.

Populate a "do_not_email.txt" file with email addresses that should not be included
in the resulting file.

When run, the code will create a file "alumni_emails.txt" that includes unique
emails that are not currently active and are not in the "do_not_email.txt" file.
