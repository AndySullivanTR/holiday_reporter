#!/usr/bin/env python3
"""
Password Reset Utility for Holiday Reporter System
Usage: python3 reset_password.py
"""

from werkzeug.security import generate_password_hash
import json
import secrets
import string

def generate_random_password(length=6):
    """Generate a random password with mixed case and numbers"""
    chars = string.ascii_letters + string.digits
    return ''.join(secrets.choice(chars) for _ in range(length))

def reset_password(username):
    """Reset password for a given username"""
    # Load reporters
    try:
        with open('data/reporters.json', 'r') as f:
            reporters = json.load(f)
    except FileNotFoundError:
        print("ERROR: data/reporters.json not found")
        return False
    
    # Check if user exists
    if username not in reporters:
        print(f"ERROR: Username '{username}' not found")
        print(f"\nAvailable usernames:")
        for user in sorted(reporters.keys()):
            if not reporters[user].get('is_manager'):
                print(f"  - {user}")
        return False
    
    # Generate new password
    new_password = generate_random_password()
    
    # Hash and update
    reporters[username]['password'] = generate_password_hash(new_password)
    
    # Save
    with open('data/reporters.json', 'w') as f:
        json.dump(reporters, f, indent=2)
    
    # Display results
    name = reporters[username].get('name', username)
    print(f"\n✓ Password reset successful!")
    print(f"  Name: {name}")
    print(f"  Username: {username}")
    print(f"  NEW PASSWORD: {new_password}")
    print(f"\nPlease provide this password to the user.\n")
    
    return True

if __name__ == "__main__":
    print("=" * 60)
    print("HOLIDAY REPORTER PASSWORD RESET UTILITY")
    print("=" * 60)
    
    username = input("\nEnter username: ").strip().lower()
    
    if not username:
        print("ERROR: No username provided")
    else:
        reset_password(username)
