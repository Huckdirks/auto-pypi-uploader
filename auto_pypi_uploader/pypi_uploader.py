# Imported Libraries
from dotenv import load_dotenv
from setup_file_creator import create_setup

# Python Libraries
from os import getenv, system, getcwd
from os.path import dirname, join, isfile
from sys import argv
from getpass import getpass

# Constants
ENV_NAME = "pypi_account_info.env"  # CHANGE THIS TO YOUR ENVIRONMENT NAME (.env file)
ENV_PATH = join(dirname(__file__), ENV_NAME)
SETUP_PATH = getcwd() + "/setup.py"


# Set up the environment file
def set_login(USERNAME: str, PASSWORD: str) -> None:
    with open(ENV_PATH, "w") as f:
        f.write(f"# PyPi Account Details\nUSERNAME = \"{USERNAME}\"\nPASSWORD = \"{PASSWORD}\"")
    return


# Export to PyPi given a version
def pypi_upload(**kwargs) -> bool:
    if (len(argv) == 2 and (argv[1].lower() == "-h" or argv[1].lower() == "--help")) or (kwargs and "help" in kwargs):  # If help is passed in, print help
        system("clear")
        print("\nPyPi Uploader Help:")
        print("\nThis program is used to automate uploading a package to PyPi. It will automatically change the version in setup.py to a passed in version, then upload the package to PyPi.")
        print("\nYou can run this program in one of two ways:")
        print("\t1. From the command line (arguments are optional):")
        print("\tUsage to upload to PyPi: python3 pypi_uploader.py [VERSION]\n\t\te.g. python3 pypi_uploader.py \"1.0.0\"")
        print("\n\tUsage to create the environment file: python3 pypi_uploader.py  [-u/--user] [USERNAME] [PASSWORD]\n\t\te.g. python3 pypi_uploader.py -u \"username\" \"password\"")
        print("\n\t2. With parameters in a function call:")
        print("\tUsage to upload to PyPi: pypi_upload(version = \"[VERSION]\")\n\t\te.g. pypi_upload(version = \"1.0.0\")")
        print("\n\tUsage to create the environment file: set_login(username = \"[USERNAME]\", password = \"[PASSWORD]\")\n\t\te.g. set_login(username = \"username\", password = \"password\")")
        print("\nIf you run this program without any parameters, it will prompt the user for the current version (and the username & password if not already saved).")
        return False
    elif len(argv) == 4 and (argv[1].lower() == "-u" or argv[1].lower() == "--user"):  # If username & password are passed in, create the environment file
        print("Created environment file")
        return set_login(argv[2], argv[3])
    elif not isfile(SETUP_PATH):  # If setup.py is not found, return False
        print(f"Setup file not found: {SETUP_PATH}")
        if len(argv) <= 1 and not kwargs:  # If in user input mode, run create_setup()
            create_setup()
        else:   # If not in user input mode, return False
            print("Either run setup_file_creator.py or import create_setup from setup_file_creator and run create_setup() to create the 'setup.py' file\nRun with [-h/--help] or pass in [help=True] to see help")
            return False
    elif not isfile(ENV_PATH):    # If the environment file is not found, or username & password aren't passed in, create the .env & return False
        print(f"Environment file not found: {ENV_PATH}")
        if len(argv) == 1 and not kwargs:  # If in user input mode, ask for username & password
            USERNAME = input("Please provide your PyPi username: ")
            PASSWORD = getpass("Please provide your PyPi password: ")
            set_login(USERNAME, PASSWORD)
        elif len(argv) == 5 and (argv[2].lower() == "-u" or argv[2].lower() == "--user"):  # If in command line mode & all parameters are passed in, use username & password passed in
            set_login(argv[3], argv[4])
        elif kwargs and ("username" in kwargs and "password" in kwargs):  # If in function call mode & all parameters are passed in, use username & password passed in
            set_login(kwargs["username"], kwargs["password"])
            if not "version" in kwargs:
                print("Please provide a package version")
                return False
        else:                          # If not in user input mode, 
            print("Either run pypi_uploader.py to manually put your pip account information in .env file before the program can continue:\n\tpython3 pypi_uploader.py -u \"username\" \"password\"\nOr pass your pip account information into the set_login() function to set up the .env file before the program can continue:\n\tset_pypi_login(username = \"username\", password = \"password\")\nRun with [-h/--help] or pass in [help=True] to see help")
            return False

    if kwargs and "version" in kwargs:  # If a version is passed in as a parameter, use that version
        PACKAGE_VERSION = kwargs["version"]
    elif len(argv) == 2 and argv[1]:    # If a version is passed in via command line arguments, use that version
        PACKAGE_VERSION = argv[1]
    elif len(argv) <= 1 and not kwargs: # If no version is passed in & in user input mode, ask for a version
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