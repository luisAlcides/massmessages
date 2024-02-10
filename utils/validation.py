

def validateUsername(username):
    if len(username) < 2:
        return False
    return True


def validatePassword(password):
    if len(password) < 5:
        return False
    return True