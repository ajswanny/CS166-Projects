# Alexander Swanson
# login_intranet.py

# Import necessary modules.
from intranet__user import User
from tkinter import Frame, Entry, Button, Tk, Label
import hashlib as hlb
import time


class IntranetGUI:

    # Create master window.
    master = Tk()

    # Create three example/test users with different access levels and usernames.
    userA = User("A", "alpha", "password1")
    userB = User("B", "beta", "password2")
    userC = User("C", "charlie", "password3")

    # Create list to contain all 'users'.
    users_list = [userA, userB, userC]

    # Initialize user access level.
    current_access_level = ""

    # Customize the window.
    master.geometry("340x300")
    master.title("BusinessX")
    master.resizable(False, False)

    # Initialize debugging variables.
    current_window = ""

    # 'Login' window. This window displays the login prompts and allows the user to create a new account.
    # noinspection PyAttributeOutsideInit
    def login_window(self):

        # Redefine troubleshooting variables.
        self.current_window = "login"

        # Create widgets for frame_one.
        # Widgets: the title label.
        self.title_label = Label(self.frame_one, text='Welcome to BusinessX Intranet')
        # Pack widgets in frame_one.
        self.title_label.pack(side='left')  # Check packing location!

        # Create the widgets for frame_two.
        # Widgets: the label indicating the 'Username' field and its corresponding entry,
        self.username_prompt_label = Label(self.frame_two, text='Username:')
        self.username_entry = Entry(self.frame_two, width='10')
        # Pack widgets.
        self.username_prompt_label.pack(side='left')
        self.username_entry.pack(side='left')

        # Create the widgets for frame_three.
        # Widgets: the label indicating the 'Password' field and its corresponding entry,
        self.password_prompt_label = Label(self.frame_three, text='Password:')
        self.password_entry = Entry(self.frame_three, width='10')
        # Pack widgets.
        self.password_prompt_label.pack(side='left')
        self.password_entry.pack(side='left')

        # Create widgets for frame four_four.
        # Widgets: the login button.
        self.login_button = Button(self.frame_four, text='Login', command=self.login)
        self.new_user_button = Button(self.frame_four, text='Create User', command=self.toggle_new_user)
        # Pack widgets.
        self.login_button.pack(side='left')
        self.new_user_button.pack(side='left')

        # Create the widgets for frame_five.
        # Widgets: the unpacked label for a new username and its corresponding entry.
        self.new_user_prompt_label = Label(self.frame_five, text='New Username: ')
        self.new_user_entry = Entry(self.frame_five, width='10')
        # Pack widgets.
        self.new_user_prompt_label.pack(side='left')
        self.new_user_entry.pack(side='left')

        # Create the widgets for frame_six.
        # Widgets: the unpacked label for a new password and its corresponding entry.
        self.new_password_prompt_label = Label(self.frame_six, text='New Password: ')
        self.new_password_entry = Entry(self.frame_six, width='10')
        # Pack widgets.
        self.new_password_prompt_label.pack(side='left')
        self.new_password_entry.pack(side='left')

        # Create the widgets for frame_seven
        # Widgets: the button to confirm the creation of a new user.
        self.new_user_confirm_button = Button(self.frame_seven, text='Confirm', command=self.create_new_user)
        self.new_user_confirm_button.pack(side='left')

    # Define method to determine login process.
    def login(self):

        # Log user in if valid credentials are provided.
        self.check_input()

    # Define method to record user input, check for validity, and grant appropriate access to menu.
    def check_input(self):

        # Store attempted login information in variables for work.
        username_input = self.username_entry.get()
        password_input = self.password_entry.get()

        # Print information to console for verification.
        print("Username input:" + username_input)
        print("Password input:" + password_input)

        # Open a text file to store login information.
        with open("login_log.txt", "a") as out:
            # Check if attempted credentials match any valid credentials.
            for obj in self.users_list:

                """
                4. To authenticate a registered user, you will modify the functionality to encrypt the password 
                entered by the user and compare it to what is stored in the csv (or txt) file.
                """
                username = obj.username
                password_hash = obj.hash_code
                attempt_pswd_hash = hlb.sha512(password_input.encode()).hexdigest()

                # Initialize menu access success variable.
                success = "False"

                # Skip current iteration if username does not correspond to the user being examined.
                if username_input != username:
                    continue

                # If username and password both match...
                if username_input == username and attempt_pswd_hash == password_hash:
                    success = "True"


                    """
                    3. Store a salted & hashed password and the  salt used in the csv (or txt) file, along with the username 
                    and access level.
                    """
                    for item in obj.out_credentials:
                        out.write(item + " / ")
                    out.write(time.strftime("%Y-%m-%d / %H:%M:%S"))
                    out.write("\n")

                    # Indicate condition to operator.
                    print("Both username and password are valid.")

                    # Set access level reference.
                    self.current_access_level = obj.access_level

                    # Grant access, proceed to menu window.
                    self.enter_menu_window()

                    break

                # If username matches but password does not.
                elif username_input == username and attempt_pswd_hash != password_hash:
                    entries = [obj.access_level, username_input, password_input, success]

                    # Write details to log.
                    for item in entries:
                        out.write(item + " / ")
                    out.write(time.strftime("%Y-%m-%d / %H:%M:%S"))
                    out.write("\n")

                    # Indicate condition to operator.
                    print("Username valid; password is not.")
                    # Possible: push message to indicate condition.

                # If password matches but username does not.
                elif username_input != username and attempt_pswd_hash == password_hash:
                    entries = ["Null", username_input, password_input, success]

                    # Write details to log.
                    for item in entries:
                        out.write(item + " / ")
                    out.write(time.strftime("%Y-%m-%d / %H:%M:%S"))
                    out.write("\n")

                    # Indicate condition to operator.
                    print("Password is valid; username is not.")
                    # Possible: push message to indicate condition.

                # If neither username nor password match.
                elif username_input != username and password_input != password_hash:
                    entries = ["Null", username_input, password_input, success]

                    for item in entries:
                        out.write(item + " / ")
                    out.write(time.strftime("%Y-%m-%d / %H:%M:%S"))
                    out.write("\n")

                    # Indicate condition to operator.
                    print("Neither username nor password are valid.")
                    # Possible: push message to indicate condition.

    # Define method to present menu of options if user enters valid credentials.
    def menu_window(self):

        # Redefine troubleshooting variables.
        self.current_window = "menu"

        # Create widgets for f1.
        title_label = Label(self.f1, text='Welcome to BusinessX Intranet')
        # Pack the widget(s).
        title_label.pack(side='left')

        # Create and pack widgets for f2 through f5.
        # Will form access interface to the four menus (given appropriate permissions).
        # (Accounting, Investments, Technology, Espionage)

        # Create 'Accounting' interface.
        self.accounting_label = Label(self.f2, text="Accounting")
        self.accounting_button = Button(self.f2, text='1', command=self.display_accounting)

        # Pack widgets.
        self.accounting_button.pack(side='left')
        self.accounting_label.pack(side='left')

        # # Create 'Investments' interface.
        self.investments_label = Label(self.f3, text="Investments")
        self.investments_button = Button(self.f3, text='2', command=self.display_investments)

        # Pack widgets.
        self.investments_button.pack(side='left')
        self.investments_label.pack(side='left')

        # Create 'Technology' interface.
        self.technology_label = Label(self.f4, text="Technology")
        self.technology_button = Button(self.f4, text='3', command=self.display_technology)

        # Pack widgets.
        self.technology_button.pack(side='left')
        self.technology_label.pack(side='left')

        # Create 'Espionage' interface.
        self.espionage_label = Label(self.f5, text="Espionage")
        self.espionage_button = Button(self.f5, text='4', command=self.display_espionage)

        # Pack widgets.
        self.espionage_button.pack(side='left')
        self.espionage_label.pack(side='left')

        # Create access-level information displays.
        self.selected_access_level = Label(self.f6, text="")
        # Pack widget.
        self.selected_access_level.pack()

        # Create logout button.
        self.logout_button = Button(self.f7, text='Logout', command=self.enter_login_window)
        # Pack widget.
        self.logout_button.pack(side='left')

    # Create function to display 'Accounting' module content.
    def display_accounting(self):

        # Adjust content.
        self.selected_access_level.config(text="Welcome to Accounting!" + "\n" + "...")

    # Create function to display 'Investments' module content.
    def display_investments(self):

        # Adjust content.
        self.selected_access_level.config(text="Welcome to the Investment Center!" + "\n" + "...")

    # Create function to display 'Technology' module content.
    def display_technology(self):

        # Verify that user has permission to view this content. Technology content requires level A or B permissions.
        if self.current_access_level == self.userC.access_level:

            # Call method to appropriately adjust content.
            self.invalid_access_c()

        else:
            # Adjust content.
            self.selected_access_level.config(text="Technology module 9X is 58% completed.")

    # Create function to display 'Espionage' module content.
    def display_espionage(self):

        # Verify that user has permission to view this content. Espionage content requires level A permission.
        if self.current_access_level == self.userB.access_level or self.current_access_level == self.userC.access_level:

            # Call method to appropriately adjust content.
            self.invalid_access_b()

        else:
            # Adjust content.
            self.selected_access_level.config(text="Agents currently proceeding with newest directive.")

    # Adjusts content for invalid access request.
    def invalid_access_c(self):

        # Deliver unauthorized access message.
        self.selected_access_level.config(text="You currently do not have" + "\n"
                                                                             " permission to view this content." + "\n" + "...")

    # Adjusts content for invalid access request.
    def invalid_access_b(self):

        # Deliver unauthorized access message.
        self.selected_access_level.config(text="You currently do not have" + "\n"
                                                                             " permission to view this content." + "\n" + "...")

    # Define method to create a new 'User' object.
    def create_new_user(self):

        # Record new credentials.
        new_username = self.new_user_entry.get()
        new_password = self.new_password_entry.get()

        # Create new user with recorded credentials.
        user_x = User("C", new_username, new_password)

        # Add user to 'users_list' for documentation.
        self.users_list.append(user_x)

        # Print users_list for debugging purposes.
        print(self.users_list)

    # Define method to adjust window display. Adjust to the 'login' window.
    def enter_login_window(self):

        # Secure appropriate window display; temporarily unpack all frames
        self.unpack_all_frames()

        # Pack the login window.
        login_window_frames = [self.frame_one, self.frame_two, self.frame_three, self.frame_four]
        for frame in login_window_frames:
            frame.pack()

    # Define method to adjust window display. Adjust to the 'menu' window.
    def enter_menu_window(self):

        # Secure appropriate window display; temporarily unpack all frames
        self.unpack_all_frames()

        # Pack the menu window.
        menu_window_frames = [self.f1, self.f2, self.f3, self.f4, self.f5, self.f6, self.f7]
        for frame in menu_window_frames:
            frame.pack()

    # Define method to forget all frames when adjusting window display.
    def unpack_all_frames(self):

        # Create list of all currently existing frames for both windows.
        frames = [self.frame_one, self.frame_two, self.frame_three, self.frame_four, self.frame_five,
                  self.frame_six, self.frame_seven, self.f1, self.f2, self.f3, self.f4, self.f5, self.f6, self.f7]

        # Forget all frames in 'frames'.
        for frame in frames:
            frame.pack_forget()

    # Define method to toggle display of widgets that enable new user creation.
    def toggle_new_user(self):

        # Pack user-creation widgets.
        self.frame_five.pack()
        self.frame_six.pack()
        self.frame_seven.pack()

    # Define initialization method.
    def __init__(self):

        # Create frames,
        # for login_window:
        self.frame_one = Frame()
        self.frame_two = Frame()
        self.frame_three = Frame()
        self.frame_four = Frame()
        self.frame_five = Frame()
        self.frame_six = Frame()
        self.frame_seven = Frame()

        # for menu window:
        self.f1 = Frame()
        self.f2 = Frame()
        self.f3 = Frame()
        self.f4 = Frame()
        self.f5 = Frame()
        self.f6 = Frame()
        self.f7 = Frame()

        # Set the main window to login_window.
        self.main_window = self.master

        # Generate 'login' and 'menu' windows.
        self.login_window()
        self.menu_window()

        # Display the 'login' window.
        self.enter_login_window()

        # Enter the tkinter main loop.
        self.master.mainloop()
