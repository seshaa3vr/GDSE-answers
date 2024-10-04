import hashlib

A= input("Enter your password: ")
c = hashlib.sha256()
c.update(A.encode())
o = c.hexdigest()
print("SHA-256 Hash of the password:", o)

