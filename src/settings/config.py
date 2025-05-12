import os


SECRET_KEY = os.environ.get("SECRET_KEY", "123")
ALGORITHM = os.environ.get("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = 2 * 30 * 24 * 60 # = 2 months

USERS = [
    {"username": "abc", "password": "123"},
]

API_VERSION = "api/0.0.1"

CLIENT_TOKEN_DURATION_IN_HOURS = 1
