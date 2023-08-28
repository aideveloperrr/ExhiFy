# ExhiFy

# Spotify Account Generator

This Python script is designed for educational purposes and demonstrates how to create Spotify accounts programmatically using the `requests` library. It generates random but realistic-looking email addresses, usernames with three random numbers at the end, and passwords. The generated account details are then saved to a file named `accs.txt`. The script runs indefinitely, creating accounts with a 3-second gap between each account generation.

## Features

- Generates realistic-looking email addresses, usernames, and passwords.
- Appends account details (username, email, password) to `accs.txt` with "|" (pipe) as a separator.
- Runs continuously until manually closed, creating accounts at a 3-second interval.

## How to Use

1. Make sure you have Python installed on your system.

2. Install the `requests` library if you haven't already:

   ```bash
   pip install requests
