import hashlib


def hash_password(password):
    password_bytes = password.encode('utf-8')
    sha256 = hashlib.sha256()
    sha256.update(password_bytes)
    hashed_password = sha256.hexdigest()
    return hashed_password


if __name__ == '__main__':
    password = hash_password('Quezada$alvaro23')
    print(password)