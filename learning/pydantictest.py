from datetime import datetime
from pydantic import BaseModel

# Pydantic model for data validation
class User(BaseModel):
    id: int  # Required field
    name: str = "John Doe"  # Optional with default
    signup_ts: datetime | None = None  # Optional datetime
    friends: list[int] = []  # List with default empty


# Data with mixed types (strings, bytes)
external_data = {
    "id": "123",  # Will convert to int
    "signup_ts": "2017-06-01 12:22",  # Will parse to datetime
    "friends": [1, "2", b"3"],  # Will convert all to int
}

# Create User - Pydantic auto-validates and converts types
user = User(**external_data)

print(user)
# > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)
# > 123


# What I learned:
# - Pydantic validates and converts data automatically
# - BaseModel creates data models with type checking
# - Default values make fields optional
# - Mixed types (str, bytes) get converted correctly
# - Reduces manual validation code