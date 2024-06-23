import random
import string
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_password(key, password):
    cipher_suite = Fernet(key)
    encrypted_password = cipher_suite.encrypt(password.encode())
    return encrypted_password

def decrypt_password(key, encrypted_password):
    cipher_suite = Fernet(key)
    decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
    return decrypted_password

def store_password(service, username, password, key, password_storage):
    encrypted_password = encrypt_password(key, password)
    password_storage[service] = {
        'username': username,
        'password': encrypted_password
    }
    print(f"Password for {service} stored securely.")

def retrieve_password(service, key, password_storage):
    if service in password_storage:
        stored_data = password_storage[service]
        decrypted_password = decrypt_password(key, stored_data['password'])
        print(f"Retrieved password for {service}: {decrypted_password}")
    else:
        print(f"No password found for {service}.")

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_password = ''.join(random.choice(characters) for i in range(length))
    return random_password


def display_menu():
    print("\nPassword Manager Menu:")
    print("1. Store a Password")
    print("2. Retrieve a Password")
    print("3. Generate a Random Password")
    print("4. Exit")
    choice = input("Enter your choice (1/2/3/4): ")
    return choice

def main():
    key = generate_key()

    password_storage = {}

    while True:
        choice = display_menu()

        if choice == '1':
            service = input("Enter the service name: ")
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            store_password(service, username, password, key, password_storage)

        elif choice == '2':
            service = input("Enter the service name to retrieve password: ")
            retrieve_password(service, key, password_storage)

        elif choice == '3':
            length = int(input("Enter the length of the password to generate: "))
            generated_password = generate_random_password(length)
            print(f"Generated password: {generated_password}")

        elif choice == '4':
            print("Exiting Password Manager.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
