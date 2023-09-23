import os
import pyAesCrypt

def lock_file(file_path, password):
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"File '{file_path}' not found.")
        return
    
    # Define the name for the encrypted file
    encrypted_file = file_path + ".aes"

    try:
        # Encrypt the file with the password
        pyAesCrypt.encryptFile(file_path, encrypted_file, password)

        # Remove the original unencrypted file (optional)
        os.remove(file_path)

        print(f"File '{file_path}' locked successfully.")
        print(f"Encrypted file '{encrypted_file}' created.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    file_path = "my.txt"
    password = input("Enter a password to lock the file: ")
    lock_file(file_path, password)
