# This module collects and validates the customer's name and contact number.

import re


def validate_name(name):
    name = name.strip()

    if not name:
        return False

    if len(name) > 100:
        return False

    # Names must contain at least one letter.
    if not any(character.isalpha() for character in name):
        return False

    return True


def validate_contact_number(number):
    number = number.strip()

    # Accept common phone-number formats, including spaces,
    # parentheses, hyphens, and an optional leading plus sign.
    if not re.fullmatch(r"\+?[0-9() -]{7,25}", number):
        return False

    # Require between 7 and 15 digits.
    digits = re.sub(r"\D", "", number)

    return 7 <= len(digits) <= 15
