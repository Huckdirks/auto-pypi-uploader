# Imported Libraries
from dotenv import load_dotenv

# Python Libraries
from os import getenv, system
from os.path import dirname, join, isfile
from sys import argv

# Constants
ENV_NAME = "pip_account_info.env"  # CHANGE THIS TO YOUR ENVIRONMENT NAME (.env file)
ENV_PATH = join(dirname(__file__), ENV_NAME)


# Set up the environment file
def set_pypi_login(USERNAME: str, PASSWORD: str) -> None:
    with open(ENV_PATH, "w") as f:
        f.write(f"# Pip Account Details\nUSERNAME = \"{USERNAME}\"\nPASSWORD = \"{PASSWORD}\"")
    return


# Export to PyPi given a version
def pypi_upload(**kwargs) -> bool:
    if len(argv) == 4 and (argv[1].lower() == "-u" or argv[1].lower() == "--user"):  # If username & password are passed in, create the environment file
        print("Created environment file")
        return set_pypi_login(argv[2], argv[3])

    elif not isfile(ENV_PATH):    # If the environment file is not found, or username & password aren't passed in, create the .env & return False
        print(f"Environment file not found: {ENV_PATH}")
        if len(argv) == 1 and not kwargs:  # If in user input mode, ask for username & password
            USERNAME = input("Please provide a PyPi username: ")
            PASSWORD = input("Please provide a PyPi password: ")
            set_pypi_login(USERNAME, PASSWORD)
        else:
            print("Please input your pip account information in the newly made .env file")
            set_pypi_login(None, None)
            return False
        
    if kwargs and "version" in kwargs:  # If a version is passed in as a parameter, use that version
        PACKAGE_VERSION = kwargs["version"]
    elif len(argv) == 2 and argv[1]:    # If a version is passed in via command line arguments, use that version
        PACKAGE_VERSION = argv[1]
    elif len(argv) == 1 and not kwargs: # If no version is passed in & in user input mode, ask for a version
        PACKAGE_VERSION = input("Please provide a package version")
    else:                               # If no version is passed in (somehow), return False
        print("Please provide a package version")
        return False
    
    # Change version in setup.py
    lines = []
    with open("setup.py", "r") as f:
        lines = f.readlines()
    
    # Find the line with "version = " and replace it with the new version
    for i, line in enumerate(lines):
        if "version = " in line:
            lines[i] = f"\tversion = \"{PACKAGE_VERSION}\",\n"
            break
    
    # Write the new lines to setup.py
    with open("setup.py", "w") as f:
        f.writelines(lines)

    # Run setup.py then begin uploading to PyPi
    system("python3 setup.py sdist bdist_wheel")

    # Get PyPi Account Variables   
    load_dotenv(ENV_PATH)
    USERNAME = getenv("USERNAME")
    PASSWORD = getenv("PASSWORD")
    system(f"twine upload dist/* -u \"{USERNAME}\" -p \"{PASSWORD}\"")
    

if __name__ == "__main__":
    pypi_upload()