def grade(arg, key):
    if key.lower().strip() == "session_cookies_are_the_most_delicious":
        return True, "You've successfully solved the problem!"
    else:
        return False, "Incorrect"