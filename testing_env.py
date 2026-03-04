# This is a test file for environment variables

from dotenv import load_dotenv
import os

load_dotenv()

print("Name:", os.getenv("MY_NAME"))
print("Secret:", os.getenv("SECRET_NUMBER"))
