import re
from rest_framework.exceptions import ValidationError

def validate_company_name(value):
    if not value or len(value.strip()) < 5:
        raise ValidationError("Company name must be at least 5 characters long.")

def validate_company_code(value):
    if value is None:
        return
    pattern = r'^[A-Za-z]{2}[0-9]{2}[EN]$'
    if not re.match(pattern, value):
        raise ValidationError(
            "Company code must be 5 characters: "
            "1st & 2nd alphabets, 3rd & 4th numbers, 5th E or N."
        )


