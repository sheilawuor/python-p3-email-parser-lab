import re

class EmailAddressParser:
    def __init__(self, email_string):
        self.email_string = email_string
    
    def parse(self):
        # Split by commas and/or spaces
        tokens = re.split(r'[,\s]+', self.email_string)
        
        # Filter for valid email addresses using regex
        email_pattern = r'^[^@]+@[^@]+\.[^@]+$'
        emails = [token for token in tokens if re.match(email_pattern, token)]
        
        # Return unique emails sorted alphabetically
        return sorted(set(emails))