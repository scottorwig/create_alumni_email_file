import os
import re

def is_valid_email(email):
    # Regular expression for validating an email
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    return re.search(regex, email)

def create_alumni_email_file():
    # Read all text files in the email_files directory
    raw_emails = []
    for filename in os.listdir('email_files'):
        if filename.endswith('.txt'):
            with open(os.path.join('email_files', filename), 'r') as f:
                raw_emails.extend(f.read().splitlines())

    # Remove duplicate emails
    raw_emails = list(set(raw_emails))

    with open('current_members.txt', 'r') as f:
        current_members = f.read().splitlines()
    with open('do_not_email.txt', 'r') as f:
        do_not_email = f.read().splitlines()

    alumni_emails = []
    for email in raw_emails:
        if is_valid_email(email) and email not in current_members and email not in do_not_email:
            alumni_emails.append(email)

    with open('alumni_emails.txt', 'w') as f:
        f.write(','.join(alumni_emails))
