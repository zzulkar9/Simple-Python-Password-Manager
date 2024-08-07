import json
import os
import getpass

# File to store passwords
PASSWORD_FILE = 'passwords.json'

# Function to load passwords from file
def load_passwords():
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, 'r') as file:
            return json.load(file)
    return {}

# Function to save passwords to file
def save_passwords(passwords):
    with open(PASSWORD_FILE, 'w') as file:
        json.dump(passwords, file, indent=4)

# Function to add a new password
def add_password():
    print("\n--- Add a New Password ---")
    website = input('Website name (or type "exit" to go back): ')
    if website.lower() == 'exit':
        return
    url = input('Website URL (or type "exit" to go back): ')
    if url.lower() == 'exit':
        return
    username = input('Username (or type "exit" to go back): ')
    if username.lower() == 'exit':
        return
    password = getpass.getpass('Password (or type "exit" to go back): ')
    if password.lower() == 'exit':
        return

    passwords = load_passwords()
    passwords[website] = {'url': url, 'username': username, 'password': password}
    save_passwords(passwords)
    print('\nPassword added successfully!')

# Function to view passwords and provide options to edit or delete
def view_passwords():
    passwords = load_passwords()
    
    if not passwords:
        print('\nNo passwords found.')
        return
    
    print("\n--- Stored Passwords ---")
    # Print table header
    print(f"{'No.':<5}{'Website':<20}{'URL':<30}{'Username':<20}{'Password':<20}")
    print('-' * 95)
    
    for i, (website, info) in enumerate(passwords.items(), 1):
        print(f"{i:<5}{website:<20}{info['url']:<30}{info['username']:<20}{info['password']:<20}")
        print('-' * 95)

    while True:
        print('\nOptions:')
        print('1. Edit a password')
        print('2. Delete a password')
        print('3. Back to main menu')
        print('4. Exit')
        choice = input('Enter your choice: ')

        if choice == '1':
            website = input('Enter the website name to edit (or type "exit" to go back): ')
            if website.lower() == 'exit':
                break
            if website in passwords:
                edit_password(website)
            else:
                print(f'No password found for {website}.')
        elif choice == '2':
            website = input('Enter the website name to delete (or type "exit" to go back): ')
            if website.lower() == 'exit':
                break
            if website in passwords:
                delete_password(website)
            else:
                print(f'No password found for {website}.')
        elif choice == '3':
            break
        elif choice == '4':
            exit_program()
        else:
            print('Invalid choice! Please try again.')

# Function to edit a password
def edit_password(website):
    passwords = load_passwords()
    if website in passwords:
        print("\n--- Edit Password ---")
        url = input(f'Enter new URL for {website} (leave blank to keep current or type "exit" to go back): ')
        if url.lower() == 'exit':
            return
        username = input(f'Enter new username for {website} (leave blank to keep current or type "exit" to go back): ')
        if username.lower() == 'exit':
            return
        password = getpass.getpass(f'Enter new password for {website} (leave blank to keep current or type "exit" to go back): ')
        if password.lower() == 'exit':
            return

        if url:
            passwords[website]['url'] = url
        if username:
            passwords[website]['username'] = username
        if password:
            passwords[website]['password'] = password

        save_passwords(passwords)
        print('Password updated successfully!')
    else:
        print(f'No password found for {website}.')

# Function to delete a password
def delete_password(website):
    passwords = load_passwords()
    if website in passwords:
        confirm = input(f'Are you sure you want to delete the password for {website}? (y/n or type "exit" to go back): ')
        if confirm.lower() == 'y':
            del passwords[website]
            save_passwords(passwords)
            print('Password deleted successfully!')
        else:
            print('Deletion canceled.')
    else:
        print(f'No password found for {website}.')

# Function to exit the program
def exit_program():
    print("Goodbye!")
    exit()

# Main menu
def main():
    while True:
        print('\n--- Password Manager Menu ---')
        print('1. Add a new password')
        print('2. View passwords')
        print('3. Exit')
        choice = input('Enter your choice: ')

        if choice == '1':
            add_password()
        elif choice == '2':
            view_passwords()
        elif choice == '3':
            exit_program()
        else:
            print('Invalid choice! Please try again.')

if __name__ == '__main__':
    main()
