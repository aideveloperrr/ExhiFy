import requests
import random
import time
import re
from datetime import datetime
from colorama import init, Fore

init(autoreset=True)

ascii_art = '''
  ______      _     _ ________     __
 |  ____|    | |   (_)  ____\ \   / /
 | |__  __  _| |__  _| |__   \ \_/ /
 |  __| \ \/ / '_ \| |  __|   \   /
 | |____ >  <| | | | | |       | |
 |______/_/\_\_| |_|_|_|       |_|
'''

throttle_interval = 3
min_password_length = 8

# Function to generate a random email address
def generate_email():
    domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'aol.com']
    username = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(8))
    domain = random.choice(domains)
    return f"{username}@{domain}"

# Function to generate a random username with 3 random numbers at the end
def generate_username():
    adjectives = ['happy', 'sunny', 'lucky', 'cool', 'smart', 'awesome']
    nouns = ['user', 'listener', 'musiclover', 'coder', 'gamer', 'explorer']
    username = f"{random.choice(adjectives)}_{random.choice(nouns)}_{random.randint(100, 999)}"
    return username

# Function to generate a random password
def generate_password():
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(characters) for _ in range(12))

# Function to validate an email address
def is_valid_email(email):
    # Using a simple regex pattern for basic email validation
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

# Function to validate a username
def is_valid_username(username):
    # Add your custom validation rules here, e.g., length constraints
    return len(username) >= 6 and len(username) <= 20

# Function to validate a password
def is_valid_password(password):
    # Add your custom validation rules here, e.g., length constraints, complexity requirements
    return len(password) >= 8


# Function to create a Spotify account and save the details
def create_and_save_spotify_account():
    username = generate_username()
    email = generate_email()
    password = generate_password()

    # Randomize birthday and ensure birth year is between 1980 and 2001
    birth_year = random.randint(1980, 2001)
    birth_month = random.randint(1, 12)
    birth_day = random.randint(1, 28)  # Assume 28 days in February for simplicity

    # Validate the generated data before proceeding
    if not is_valid_username(username):
        print(Fore.RED + f"Invalid username: {username}")
        return
    if not is_valid_email(email):
        print(Fore.RED + f"Invalid email: {email}")
        return
    if not is_strong_password(password):
        print(Fore.RED + "Weak password: Password must be at least 8 characters long and include numbers and symbols.")
        return

    # Define the Spotify registration endpoint
    signup_url = 'https://www.spotify.com/us/signup/'

    # Set up session to maintain cookies
    session = requests.Session()

    # Send GET request to get initial cookies
    session.get(signup_url)

    # Extract the CSRF token from cookies
    csrf_token = session.cookies.get('csrf_token')

    # Create a payload with user data
    payload = {
        'csrf_token': csrf_token,
        'creation_flow': 'https://www.spotify.com/us/signup/',
        'forward_url': '',
        'iagree': 'true',
        'password': password,
        'password_repeat': password,
        'birth_day': birth_day,
        'birth_month': birth_month,
        'birth_year': birth_year,
        'displayname': username,
        'email': email,
        'platform': 'www',
        'referrer': 'https://www.spotify.com/us/signup/',
        'thirdpartyemail': 'false',
        'username': username,
    }

    # Send POST request to create the Spotify account
    response = session.post(signup_url, data=payload)

    if response.status_code == 200:
        account_info = f"Email: {email} | Password: {password}"
        with open('accs.txt', 'a') as file:
            file.write(account_info + "\n")
        with open('accData.txt', 'a') as data_file:
            current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data_info = f"Email: {email} | Password: {password} | Birthdate: {birth_year}-{birth_month:02d}-{birth_day:02d} | Created: {current_date}"
            data_file.write(data_info + "\n")
        print(Fore.GREEN + f"Account created: Email: {email} | Password: {password}")
    else:
        print(Fore.RED + f"Failed to create an account for {username}")

    # Throttle the script to avoid excessive requests
    time.sleep(throttle_interval)

def is_strong_password(password):
    # Check if the password meets the minimum length requirement
    if len(password) < min_password_length:
        return False

    # Check if the password contains at least one digit
    if not any(char.isdigit() for char in password):
        return False

    # Check if the password contains at least one symbol (e.g., !, @, #, $, etc.)
    if not any(char.isalnum() for char in password):
        return False

    return True

print(ascii_art)
print("Version: V2.0")
time.sleep(5)

account_count = 0


# Run the script indefinitely with a 3-second gap between each account creation
while True:
    create_and_save_spotify_account()
    account_count += 1
    print(f"Accounts created: {account_count}")
