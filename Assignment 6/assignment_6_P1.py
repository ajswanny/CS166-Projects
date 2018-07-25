# Alexaner Swanson
# CS 166 - Cybersecurity Principles
# Professor James Eddy
# Assignment 6 - Part I

# Import necessary modules.
import hashlib
from random import randint

# Generate the (hexidecimal) hash using the identified algorithm for the following passwords:
p1_hash = hashlib.md5(b'letMeIn').hexdigest()
p2_hash = hashlib.md5(b'admin').hexdigest()
p3_hash = hashlib.sha1(b'gr8tPW').hexdigest()
p4_hash = hashlib.sha256(b'hello123').hexdigest()
p5_hash = hashlib.sha512(b'v@ry$ecURE!').hexdigest()

# Create a list of the hashed plaintext password.
hashed_passwords = [p1_hash, p2_hash, p3_hash, p4_hash, p5_hash]

# Output each of the hashes.
for i in hashed_passwords:
    print(i)