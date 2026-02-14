import random
import string
import hashlib
from datetime import datetime

def generate_password(length=14):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def log_action(action):
    with open("audit.log", "a") as log:
        log.write(f"{datetime.now()} - {action}\n")

