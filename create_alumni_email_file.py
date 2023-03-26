import os
import re

def is_valid_email(email):
    # Regular expression for validating an email
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    return re.search(regex, email)

def create_alumni_email_file():
    # Read all .txt and .csv files in the past_member_files directory
    raw_emails = []
    for filename in os.listdir('past_member_files'):
        if filename.endswith('.txt') or filename.endswith('.csv'):
            with open(os.path.join('past_member_files', filename), 'r') as f:
                file_content = f.read()
                # Extract all valid emails from the file content
                emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', file_content)
                raw_emails.extend(emails)

    # Remove duplicate emails
    raw_emails = list(set(raw_emails))

    # Read all .txt and .csv files in the current_members directory
    current_members = []
    for filename in os.listdir('current_members'):
        if filename.endswith('.txt') or filename.endswith('.csv'):
            with open(os.path.join('current_members', filename), 'r') as f:
                file_content = f.read()
                # Extract all valid emails from the file content
                emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', file_content)
                current_members.extend(emails)

    # Remove duplicate emails
    current_members = list(set(current_members))

    with open('do_not_email.txt', 'r') as f:
        do_not_email = f.read().splitlines()

    alumni_emails = []
    for email in raw_emails:
        if is_valid_email(email) and email not in current_members and email not in do_not_email:
            alumni_emails.append(email)

    with open('alumni_emails.txt', 'w') as f:
        f.write(','.join(alumni_emails))