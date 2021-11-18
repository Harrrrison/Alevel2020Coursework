import hashlib

password = input("what is your password: ")
print(hashlib.sha256(password.encode('UTF-8')).hexdigest())