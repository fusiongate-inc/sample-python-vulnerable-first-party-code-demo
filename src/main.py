from src.db import create_db, add_user, get_user_by_id
from src.auth import create_user_profile, load_user_profile, hash_password
import os

def main():
    print("User Service Starting...")

    create_db()

    add_user("alice", 30)
    add_user("bob", 22)

    user = get_user_by_id(1)
    print("User 1:", user)

    create_user_profile_result = create_user_profile("alice")
    if create_user_profile_result:
        print("User profile created successfully for alice")
    else:
        print("Failed to create user profile for alice")

    load_user_profile_result = load_user_profile("alice")
    if load_user_profile_result:
        print("User profile loaded successfully for alice")
    else:
        print("Failed to load user profile for alice")

    password = "securepassword"
    password_hash = hash_password(password)
    print("Password hash:", password_hash)

if __name__ == "__main__":
    main()