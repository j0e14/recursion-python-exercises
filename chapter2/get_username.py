def getUsername(email):
    s = email
    at = s.find("@")
    return s[0:at]

print(getUsername("alice@gmail.com"))
