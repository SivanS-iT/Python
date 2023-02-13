import random
import string

def generate_password(length, include_capitals, include_specials):
    # Define the characters to choose from based on user preferences
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_capitals else ''
    specials = string.punctuation if include_specials else ''
    
    # Combine the characters into one string
    chars = lowercase + uppercase + string.digits + specials
    
    # Generate the password
    password = ''.join(random.choice(chars) for i in range(length))
    
    return password


password = generate_password(45, True, True)
print(password)