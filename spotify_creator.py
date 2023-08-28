import requests
import random
import time


ascii_art = '''
  ______      _     _ ________     __
 |  ____|    | |   (_)  ____\ \   / /
 | |__  __  _| |__  _| |__   \ \_/ /
 |  __| \ \/ / '_ \| |  __|   \   /
 | |____ >  <| | | | | |       | |
 |______/_/\_\_| |_|_|_|       |_|  
'''


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

# Function to create a Spotify account and save the details
def create_and_save_spotify_account():
    username = generate_username()
    email = generate_email()
    password = generate_password()

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
        'gender': 'male',  # Change as needed
        'iagree': 'true',
        'password': password,
        'password_repeat': password,
        'birth_day': '1',  # Change as needed
        'birth_month': '1',  # Change as needed
        'birth_year': '1990',  # Change as needed
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
        account_info = f"Username: {username} | Email: {email} | Password: {password}"
        with open('accs.txt', 'a') as file:
            file.write(account_info + "\n")
        print(f"Account created: {account_info}")
    else:
        print(f"Failed to create an account for {username}.")


print(ascii_art)
print("Version: V2.0")
time.sleep(5)

account_count = 0


# Run the script indefinitely with a 3-second gap between each account creation
while True:
    create_and_save_spotify_account()
    account_count += 1
    print(f"Accounts created: {account_count}")
    time.sleep(3)  # Wait for 3 seconds before creating the next account
