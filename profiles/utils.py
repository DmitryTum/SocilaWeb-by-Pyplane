import uuid


def get_random_code():
    code = str(uuid.uuid3)[:8].replace('-', '').lower()
    return code
