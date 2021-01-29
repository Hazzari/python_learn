import os
from pathlib import Path

from dotenv import load_dotenv

a = Path(__file__).parent / ".env"

if os.path.exists(a):
    load_dotenv(a)

print(os.environ.get("HELLO", "123") )
