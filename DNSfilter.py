# This script need to be executed as Administrator
import winreg
import subprocess

# Define the safe DNS server address
# Yandex
primary_dns = "77.88.8.8"
secondary_dns = "77.88.8.1"

# Function to set DNS settings
def set_dns_settings(primary, secondary):
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters", 0, winreg.KEY_WRITE)
    winreg.SetValueEx(key, "NameServer", 0, winreg.REG_SZ, primary + "," + secondary)
    winreg.CloseKey(key)

# Function to flush DNS cache (requires administrative privileges)
def flush_dns_cache():
    subprocess.run(["ipconfig", "/flushdns"], capture_output=True, text=True, check=True)

if __name__ == "__main__":
    try:
        set_dns_settings(primary_dns, secondary_dns)
        print("DNS settings updated successfully.")
        flush_dns_cache()
        print("DNS cache flushed.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")