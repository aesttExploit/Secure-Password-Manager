from auth import register, login

from vault import (
    save_password,
    view_passwords,
    update_password,
    delete_password,
    search_password
)

from password_generator import generate_password
from password_checker import check_password_strength
from audit import log_action


def main():

    while True:

        print("\n====================================")
        print("          PASSWORD MANAGER")
        print("====================================")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":

            username = input("Enter username: ")
            password = input("Enter password: ")

            success, message = register(username, password)

            print(message)

            if success:
                log_action(username, "User Registered")

        elif choice == "2":

            attempts = 3
            user_id = None

            while attempts > 0:

                username = input("Enter username: ")
                password = input("Enter password: ")

                user_id = login(username, password)


                if user_id:

                    log_action(username, "Login Successful")

                    print("\nLogin successful!")
                    break


                else:

                    attempts -= 1

                    log_action(
                        username,
                        "Failed login attempt"
                    )

                    print("\nIncorrect username or password.")
                    print(f"Attempts remaining: {attempts}")


            if attempts == 0:

                log_action(
                    username,
                    "Account locked after multiple failed login attempts"
                )

                print("\nToo many failed login attempts.")
                print("Returning to Main Menu...")
                continue



            # PASSWORD VAULT MENU

            while True:

                print("\n====================================")
                print("           PASSWORD VAULT")
                print("====================================")
                print("1. Save Password")
                print("2. View Passwords")
                print("3. Update Password")
                print("4. Delete Password")
                print("5. Generate Strong Password")
                print("6. Search Password")
                print("7. Logout")


                option = input("Choose an option: ").strip()



                if option == "1":

                    site = input("Website: ")
                    account_username = input("Website Username: ")
                    account_password = input("Website Password: ")


                    strength = check_password_strength(account_password)

                    print(f"Password Strength: {strength}")


                    save_password(
                        user_id,
                        site,
                        account_username,
                        account_password,
                        password
                    )


                    log_action(
                        username,
                        f"Saved password for {site}"
                    )



                elif option == "2":

                    view_passwords(
                        user_id,
                        password
                    )

                    log_action(
                        username,
                        "Viewed passwords"
                    )



                elif option == "3":

                    site = input("Enter website to update: ")
                    new_password = input("Enter new password: ")


                    update_password(
                        user_id,
                        site,
                        new_password,
                        password
                    )


                    log_action(
                        username,
                        f"Updated password for {site}"
                    )



                elif option == "4":

                    site = input("Enter website to delete: ")


                    delete_password(
                        user_id,
                        site
                    )


                    log_action(
                        username,
                        f"Deleted password for {site}"
                    )



                elif option == "5":

                    length = input(
                        "Enter password length (default 16): "
                    )


                    if length == "":
                        length = 16
                    else:
                        length = int(length)


                    generated_password = generate_password(length)


                    print("\nGenerated Password:")
                    print(generated_password)



                elif option == "6":

                    site = input(
                        "Enter website to search: "
                    )


                    search_password(
                        user_id,
                        site,
                        password
                    )


                    log_action(
                        username,
                        f"Searched password for {site}"
                    )



                elif option == "7":

                    log_action(
                        username,
                        "Logged out"
                    )

                    print("Logged out.")

                    break



                else:

                    print("Invalid option.")



        elif choice == "3":

            print("Exiting... Bye!")
            break



        else:

            print("Invalid choice.")



if __name__ == "__main__":
    main()