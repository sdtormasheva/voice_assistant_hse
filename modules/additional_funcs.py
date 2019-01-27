import re


def clear_address(text):
    address = re.sub(r'[^\w\s]+', ' ', text).lower()
    address_clean = re.sub(r'[\s]+', ' ', address).strip()
    return address_clean
