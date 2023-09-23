import os
import pyAesCrypt

def decrypt_file(encrypted_file, password):
    # Check if the encrypted file exists
    if not os.path.exists(encrypted_file):
        print(f"Encrypted file '{encrypted_file}' not found.")
        return

    try:
        # Extract the original file name without the ".aes" extension
        file_name, _ = os.path.splitext(encrypted_file)

        # Decrypt the file with the provided password
        pyAesCrypt.decryptFile(encrypted_file, file_name, password)

        print(f"File '{file_name}' decrypted successfully.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    encrypted_file = "my.txt.aes"  # Replace with the actual encrypted file path
    password = input("Enter the password to decrypt the file: ")
    decrypt_file(encrypted_file, password)