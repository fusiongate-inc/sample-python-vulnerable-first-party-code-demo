import bcrypt
import os
import json

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password.decode()

def create_user_profile(username):
    profile = {"username": username, "theme": "light"}
    profile_path = os.path.join("profiles", f"{username}.json")
    os.makedirs(os.path.dirname(profile_path), exist_ok=True)
    with open(profile_path, "w") as f:
        json.dump(profile, f)

def load_user_profile(username):
    profile_path = os.path.join("profiles", f"{username}.json")
    try:
        with open(profile_path, "r") as f:
            profile = json.load(f)
            print(f"Loaded profile for {username}: {profile}")
    except FileNotFoundError:
        print("Profile not found.")
    except json.JSONDecodeError:
        print("Error: Invalid profile data.")