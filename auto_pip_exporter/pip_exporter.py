# Imported Libraries
from dotenv import load_dotenv

# Python Libraries
from os import getenv
from os.path import dirname, join, isfile
from sys import argv
from time import sleep

# Constants
ENV_NAME = "pip_account_info.env"  # CHANGE THIS TO YOUR ENVIRONMENT NAME (.env file)
ENV_PATH = join(dirname(__file__), ENV_NAME)

# Main Function
def pip_exporter(**kwargs) -> bool:
    if not isfile(ENV_PATH):    # If the environment file is not found, create it & return False
        print(f"Environment file not found: {ENV_PATH}\nPlease input your pip account information in the newly made .env file")
        with open(ENV_PATH, "w") as f:
            f.write("# Pip Account Details\nUSERNAME = \nPASSWORD = ")
        return False
    if not kwargs:  # If the version is not provided, return False
        if len(argv) == 2:
            pass
        else:
            print("Please provide a package version")
            return False

    # Get Environment Variables   
    load_dotenv(ENV_PATH)
    USERNAME = getenv("USERNAME")
    PASSWORD = getenv("PASSWORD")

    # Get Version for pip package
    if argv[1]:
        PACKAGE_VERSION = argv[1]
    elif "version" in kwargs:
        PACKAGE_VERSION = kwargs["version"]
    else:
        print("Please provide a package version")
        return False
    
    # Change version in setup.py
    lines = []
    with open("setup.py", "r") as f:
        lines = f.readlines()
    
    # Find the line with "\tversion = " and replace it with the new version
    for i, line in enumerate(lines):
        if "version = " in line:
            lines[i] = f"\tversion = '{PACKAGE_VERSION}',\n"
            break
    
    # Write the new lines to setup.py
    with open("setup.py", "w") as f:
        f.writelines(lines)
    


if __name__ == "__main__":
    pip_exporter()