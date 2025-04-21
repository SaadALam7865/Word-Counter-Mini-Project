
# ✅ Project: Email Extractor App (Regex-based)
# User koi bhi text input kare — hum usme se email addresses extract karein using re module.


import re
def extract_email(text):
    # Step 1: Pattern for email addresses
    pattern = r'\b[\w.-]+@[\w.-]+\.\w{2,4}\b'

    # Step 2: Use re.findall to extract all matches
    email = re.findall(pattern, text)

    return email

# Step 3: Take input from the user
user_input = input("Paste your text here:\n")

# Step 4: Call the function
found_emails = extract_email(user_input)

# Step 5: Show results
if found_emails:
    print('\n✅ Found Emails:')
    for email in found_emails:
        print('📧', email)
else:
    print('\n❌ No email addresses found.')