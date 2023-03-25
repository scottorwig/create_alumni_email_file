import re

def is_valid_email(email):
    # Regular expression for validating an email
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    return re.search(regex, email)

def create_alumni_email_file():
    with open('raw_emails.txt', 'r') as f:
        raw_emails = f.read().splitlines()
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
