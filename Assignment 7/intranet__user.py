# Alexander Swanson
# intranet__user.py

# Import necessary modules.
import hashlib as hlb
import regex as re
from random import randint


# The class 'User' describes a user object to be used with the 'Business Intranet' GUI. Users
# can be created using the Intranet, and they carry an access level, username, password, and encrypted passsword.
class User(object):

    # Define fields.
    access_level: str = ""          # The user's access level.
    username: str = ""              # The user's username.
    plaintext_password: str = ""    # The user's plaintext password.
    salt: str = ""                  # The salt for encryption.
    salted_plaintext: str = ""      # The salted plaintext password.
    hash_code: str = ""             # The hashed plaintext password.
    salted_hash_code: str = ""      # THe salted hash.

    num_plaintext_search: list      # List to store integers for verification of valid password choice.
    credentials: list = []          # List to store all credentials.
    out_credentials: list = []      # List to store all credentials to be logged in "login_log.txt".


    # Initialization function determines specified fields.
    def __init__(self, level: str, new_username: str, new_password: str):

        username_attempt: str = new_username
        password_attempt: str = new_password

        # If credentials are valid, create object.
        if self.validate_credentials(username_attempt, password_attempt):
            self.username = new_username
            self.plaintext_password = new_password
            self.encrypt()

        elif (self.validate_credentials()) is False:
            # Inform user that their desired credentials are invalid.
            print("Operation could not be completed. Password credentials are not valid. Try again.")

            # Exit method.
            return

        # Set user's access level.
        if level != "C":
            self.access_level = level
        else:
            # Set default access level.
            self.access_level = "C"

        # Create records.
        self.credentials = [self.access_level,
                            self.username,
                            self.plaintext_password,
                            self.salt,
                            self.salted_plaintext,
                            self.hash_code,
                            self.salted_hash_code]

        self.out_credentials = [self.access_level,
                                self.username,
                                self.salt,
                                self.salted_plaintext,
                                self.hash_code]

        # Output credential records for debugging purposes.
        # print (self.out_credentials)


    # Generate encryption processes.
    def encrypt(self):

        """
        1. Generate pseudo-random salt, salted plaintext password, and hashed plaintext password.
        2. Replace the encryption algorithm you developed with the cryptographic hash function SHA-512.
        """
        # Generate pseudo-random salt.
        self.salt = str(randint(100, 500)) + "protocol" + str(randint(4, 40))

        # Store salted and hashed plaintext password.
        self.salted_plaintext = self.plaintext_password + self.salt
        self.hash_code = hlb.sha512(self.plaintext_password.encode()).hexdigest()

        # Hash salted plaintext.
        self.salted_hash_code = hlb.sha512(self.salted_plaintext.encode()).hexdigest()


    # Check user desired password for valid length and necessary characters.
    @staticmethod
    def validate_credentials(username_attempt: str, password_attempt: str):

        # Specifically initialize the integer search in the 'User' object's password.
        num_plaintext_search = re.findall('\d+', password_attempt)

        # Print to console for debugging.
        for item in num_plaintext_search:
            print("Integers in", username_attempt, ":", item)

        if re.search('[a-zA-Z]', username_attempt) is None:
            return False

        elif num_plaintext_search is None:
            return False

        elif len(password_attempt) < 8 or len(password_attempt) > 20:
            return False

        else:
            print("hi")
            return True
