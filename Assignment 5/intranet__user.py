# Created by Alexander Swanson on October 21, 2017.

# Import necessary modules.
import regex as re

# The class 'User' describes a user object to be used with the 'Business Intranet' GUI. Users
# can be created using the Intranet, and they carry an access level, username, password, and encrypted passsword.
class User(object):
    # Define fields.
    access_level = None  # The user's access level.
    username = None  # The user's username.
    password = ""  # The user's plaintext password.
    encrypted_password = ""  # The user's encrypted password.
    deciphered_password = ""  # The user's deciphered password.
    num_search = []  # The integers in the user's password. Used in 'encrypt()' as an encryption parameter.

    # Initialization function determines specified fields.
    def __init__(self, level: str, new_username: str, new_password: str):

        # If credentials are valid, create object.
        if self.validate_credentials(new_password):

            self.username = new_username
            self.password = new_password
            self.encrypt(self.num_search)
        else:

            # Inform user that their desired credentials are invalid.
            print("Operation could not be completed. Password credentials are not valid. Try again.")

            # Exit method.
            return

        # Print to console for debugging.
        for item in self.num_search:
            print("Integers in", new_username, ":", item)

        # Set user's access level.
        if level != "C":
            self.access_level = level
        else:
            # Set default access level.
            self.access_level = "C"

    # Check user desired password for valid length and necessary characters.
    @staticmethod
    def validate_credentials(password):

        # Specifically initialize the integer search in the 'User' object's password.
        num_search = re.findall('\d+', password)

        if re.search('[a-zA-Z]', password) is None or num_search is None:
            return False

        elif len(password) < 8 or len(password) > 20:
            return False

        else:
            return True

    # Define password encryption variables.

    # The decipher key.
    d = 0
    # The encryption key.
    e = 0
    # Encryption key parameter... This parameter is equal to the length of the user's password.
    k = len(password)
    # Encryption key parameter... This parameter is equal to the summed integers in the user's password.
    n = 0

    # Define 'plaintext' password for encryption and decipher use, and parameter to hold cyphered password.
    P = password
    C = ""

    # Define method to encrypt password.
    def encrypt(self, num_search: list):

        # Set 'n'.
        for x in num_search:
            self.n += int(x)

        # Define unified parameter for encryption key.
        i = self.n + self.k

        # Define encryption key.
        self.e = pow(self.n, i)

        # Display key to console for debugging purposes.
        # print("The key:", self.e)

        # Define encrypted password.
        self.C = self.password + str(self.e)

        # Print variables for debugging purposes.
        print("So: ", self.C, "\t", self.P)

        # Set encrypted password value.
        self.encrypted_password = self.C

        # Return encrypted password.
        return self.C

    def decipher(self):

        # Define decipher key.
        self.d = len(str(self.e))

        # Decipher password.
        self.P = self.C[:-self.d]

        # Return deciphered password.
        return self.P
