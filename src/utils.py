import bcrypt
import re

def run_python_code(code):
    # Validate and sanitize the input code
    if not re.match(r'^[\w\s\+\-\*\/\(\)\.=,:<>]+$', code):
        raise ValueError("Invalid code input")
    try:
        compiled_code = compile(code, '<string>', 'eval')
        eval(compiled_code)
    except Exception as e:
        print(f"Error executing code: {e}")

def hash_password(password):
    """
    Hash the given password using bcrypt.

    Args:
        password (str): The password to be hashed.

    Returns:
        str: The hashed password.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password.decode()