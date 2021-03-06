# Alexaner Swanson
# CS 166 - Cybersecurity Principles
# Professor James Eddy
# Assignment 6 - Part II

# Import necessary modules.
import hashlib
from random import randint

# Define variables for work.
password_plaintext = "helpdesk"
salt = "cyber"
pass_w_salt = password_plaintext + salt
psd_rand_pswd = str(randint(100, 500)) + "passwords" + str(randint(4, 40)) 

# Generate hash for 'helpdesk'.
pass_helpdesk_hashed = hashlib.md5(password_plaintext.encode()).hexdigest()
print(pass_helpdesk_hashed)

# 1. Add the salt 'cyber' to the end of the md5 hash for the password: 'helpdesk'.
helpdesk_hash_salted = pass_helpdesk_hashed + salt
print(helpdesk_hash_salted)

# 2. Generate the md5 hash of the salt 'cyber' and add it to the end of the md5 hash for the password: 'helpdesk'.
salt_hashed = hashlib.md5(salt.encode()).hexdigest()
print(salt_hashed)

pass_hash_w_salt_hash = pass_helpdesk_hashed + salt_hashed
print(pass_hash_w_salt_hash)

# 3. Generate the md5 hash of the password + salt (which is 'helpdesk' concatenated with the salt 'cyber').
salted_pass_hash = hashlib.md5(pass_w_salt.encode()).hexdigest()
print(salted_pass_hash)

# 4. Generate a pseudeo-random salt, add it to the end of the password 'helpdesk' and generate the md5 
#	 hash of the password + hash combination. Explain how you generated the pseudo-random salt.
#		
#		This pseudo-random salt is generated by concatenating two pseudo-random integers with the string "passwords".
psd_rand_salted_pswd = password_plaintext + psd_rand_pswd
print(psd_rand_salted_pswd)

psd_rand_salted_pswd_hash = hashlib.md5(psd_rand_salted_pswd.encode()).hexdigest()
print(psd_rand_salted_pswd_hash)

# How does salting passwords make them more secure?
# 	Salting passwords significantly increases their security on multiple fronts. These salts will exponentially 
#	increase the amount of man-hours required to crack the passwords using brute force. Moreover, salts will
# 	reduce the possibility of success for collision conditions, as these salted passwords will of course 
#	generate a hash different from the original password, so that an attackers chances of finding a matching
#	hash solution are less likely.