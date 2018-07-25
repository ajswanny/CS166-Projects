# Alexaner Swanson
# CS 166 - Cybersecurity Principles
# Professor James Eddy
# Assignment 6 - Part III

# Import necessary modules.
import hashlib

# Define 'HASH' constant.
HASH = "cc8b1415557f58abf2e2fa83c2ea6c91"

# Open 'wordlist800.txt'.
f_wordlist = open('wordlist800.txt')

# Iterate through 'wordlist800.txt' to find a hash match.
for line in f_wordlist:

	code = line.rstrip("\n")

	hashed_code = hashlib.md5(code.encode()).hexdigest()

	if hashed_code == HASH:
		print "Success. The plaintext is:", code


# Close 'wordlist800.txt'.
f_wordlist.close()