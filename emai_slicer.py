#introduces string split method

def email_splicer(email):
    (username,domain) = email.split("@")
    (domain,extension) = email.split(".")
    return {"username":username,"domain":domain,"extension":extension}

dict = email_splicer("test@gmail.com")
print(dict.get("username"))