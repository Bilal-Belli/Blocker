import os

def lock_file_for_writing(file_path):
    try:
        # Get the absolute path of the file
        abs_file_path = os.path.abspath(file_path)

        # Set the file permissions to read-only
        os.chmod(abs_file_path, 0o444)

        print(f"Write access to '{abs_file_path}' is now locked.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    file_path = r"C:\Windows\System32\drivers\etc\hosts"  # Replace with the actual path to your file
    lock_file_for_writing(file_path)
