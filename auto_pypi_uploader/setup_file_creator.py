# Python Libraries
from os import getcwd, system
from sys import argv

# Constants
FILE_NAME = "setup.py" 
FILE_PATH = getcwd() + "/" + FILE_NAME


# Create a setup.py file
def create_setup(**kwargs) -> bool:
    if kwargs and (not "name" in kwargs or not "version" in kwargs or not "author" in kwargs or not "description" in kwargs):   # If minimum required parameters are not provided, return False
        print("Please provide the minimum required parameters: name, version, author, & description\ne.g. setup_file_creator(name=\"auto-pypi-exporter\", version=\"1.0.0\", author=\"Huck Dirksmeier\", description=\"A program to automate changing a pip package's version & publishing it\")")
        return False
    elif (len(argv) > 1 and len(argv) < 5) or kwargs: # If able to be passed in parameters, possibly display help
        if (len(argv) > 1 and (argv[1].lower() == "-h" or argv[1].lower() == "--help")) or (kwargs and ("help" in kwargs and kwargs["help"] == True)):
            # Give info on how to use the program
            system("clear")
            print("\n'setup.py' Creator Help:")
            print("\nThis program creates a setup.py file in the current working directory for a Python package")
            print("\nYou can run this program in one of two ways:")
            print("\t1. From the command line (arguments are optional):")
            print("\tUsage: python3 setup_file_creator.py -n/--name NAME -v/--version \"0.0.0\" -a/--author \"AUTHOR\" -d/--description \"DESCRIPTION\"")
            print("\n\t2. With parameters in a function call:")
            print("\tUsage: setup_file_creator(name = \"NAME\", version = \"0.0.0\", author = \"AUTHOR\", description = \"DESCRIPTION\")")
            print("\nThis program has four required parameters:")
            print("\t1. [-n/--name] or name: The name of the package")
            print("\t2. [-v/--version] or version: The version of the package")
            print("\t3. [-a/--author] or author: The author of the package")
            print("\t4. [-d/--description] or description: The description of the package")
            print("\nIt can also take some optional parameters:")
            print("\t1. [-h/--help] or help: This help message")
            print("\t2. [-l/--long_description_content_type] or long_description_content_type: The long description type of the package (default: \"text/markdown\")")
            print("\t3. [-u/--url] or url: The URL to the website or GitHub repository for the project")
            print("\t4. [-i/--install_requires] install_requires: The necessary packages to install for the package to work")
            print("\t\t- Must be in a comma-separated list for Command Line Arguments, or a list for Function Call")
            print("\t5. [-k/--keywords] or keywords: The keywords for the package")
            print("\t\t- Must be in a comma-separated list for Command Line Arguments, or a list for Function Call")
            print("\t6. [-c/--classifiers] or classifiers: The classifiers for the package")
            print("\t\t- Must be in a comma-separated list for Command Line Arguments, or a list for Function Call")
            print("\t7. [-p/--python_requires] or python_requires: The minimum Python version required to run the package")
            print("\nHere's how to use all the parameters:")
            print("\tCommand Line Arguments:\n\tpython3 setup_file_creator.py -n NAME -v \"0.0.0\" -a \"AUTHOR\" -d \"DESCRIPTION\" -l \"LONG DESCRIPTION CONTENT TYPE\" -u \"WEBSITE\" -i \"PUT, PACKAGES, HERE\" -k \"KEYWORDS, HERE\" -c \"PUT, CLASSIFIERS, HERE\" -p \"PYTHON VERSION\"")
            print("\n\tPassing into Function:\n\tsetup_file_creator(name = \"NAME\", version = \"0.0.0\", author = \"AUTHOR\", description = \"DESCRIPTION\", long_description_content_type = \"LONG DESCRIPTION CONTENT TYPE\", url = \"WEBSITE\", install_requires = [\"PUT\", \"PACKAGES\", \"HERE\"], keywords = [\"KEYWORDS\", \"HERE\"], classifiers = [\"PUT\", \"CLASSIFIERS\", \"HERE\"], python_requires = \"PYTHON VERSION\")")
            print("\nIf you do not provide any parameters, the program will ask you for them")
            print("The program will automatically create a setup.py file in the current directory if one is not found")
            print("If a setup.py file is found, it will be overwritten")
            return False
        elif len(argv) > 1 or (kwargs and (not "name" in kwargs or not "version" in kwargs or not "author" in kwargs or not "description" in kwargs)):   # If parameters are provided, but not the minimum required parameters, return False
            print("\nPlease provide the minimum required parameters: name, version, author, & description")
            print("\te.g. setup_file_creator(name=\"auto-pypi-exporter\", version=\"1.0.0\", author=\"Huck Dirksmeier\", description=\"A program to automate changing a pip package's version & publishing it\")\n")
            print("Run \"python3 setup_file_creator.py -h\" or \"setup_file_creator(help = True)\" for more information")
            return False
    
    # Setting up variables

    # Optional Parameters
    long_description_content_type = "text/markdown"
    url = ""
    install_requires = []
    keywords = []
    classifiers = []
    python_requires = ""

    if kwargs:    # If parameters passed in from the function call
        NAME = kwargs["name"]
        VERSION = kwargs["version"]
        AUTHOR = kwargs["author"]
        DESCRIPTION = kwargs["description"]
        if "long_description_content_type" in kwargs:
            long_description_content_type = kwargs["long_description_content_type"]
        if "url" in kwargs:
            url = kwargs["url"]
        if "install_requires" in kwargs:
            install_requires = kwargs["install_requires"]
        if "keywords" in kwargs:
            keywords = kwargs["keywords"]
        if "classifiers" in kwargs:
            classifiers = kwargs["classifiers"]
        if "python_requires" in kwargs:
            python_requires = kwargs["python_requires"]

    elif len(argv) > 5: # If parameters passed in as command line arguments
        for i, arg in enumerate(argv):
            if arg == "-n" or arg == "--name":
                NAME = argv[i + 1]
            elif arg == "-v" or arg == "--version":
                VERSION = argv[i + 1]
            elif arg == "-a" or arg == "--author":
                AUTHOR = argv[i + 1]
            elif arg == "-d" or arg == "--description":
                DESCRIPTION = argv[i + 1]
            elif arg == "-l" or arg == "--long_description_content_type":
                long_description_content_type = argv[i + 1]
            elif arg == "-u" or arg == "--url":
                url = argv[i + 1]
            elif arg == "-i" or arg == "--install_requires":
                install_requires = argv[i + 1].split(",")
            elif arg == "-k" or arg == "--keywords":
                keywords = argv[i + 1].split(",")
            elif arg == "-c" or arg == "--classifiers":
                classifiers = argv[i + 1].split(",")
            elif arg == "-p" or arg == "--python_requires":
                python_requires = argv[i + 1]

    else:   # If no parameters passed in (in user input mode)
        NAME = input("Program Name: ")
        VERSION = input("Version: ")
        AUTHOR = input("Author: ")
        DESCRIPTION = input("Description: ")
        LONG_DESCRIPTION_CONTENT_TYPE_QUESTION = input("\nWould you like to provide a long description content type (default: \"text/markdown\")? (y/n): ")
        if LONG_DESCRIPTION_CONTENT_TYPE_QUESTION.lower() == "y" or LONG_DESCRIPTION_CONTENT_TYPE_QUESTION.lower() == "yes":
            long_description_content_type = input("Long Description Content Type: ")
        URL_QUESTION = input("\nWould you like to provide a URL? (y/n): ")
        if URL_QUESTION.lower() == "y" or URL_QUESTION.lower() == "yes":
            url = input("URL: ")
        INSTALL_REQUIRES_QUESTION = input("\nWould you like to provide packages to install? (y/n): ")
        if INSTALL_REQUIRES_QUESTION.lower() == "y" or INSTALL_REQUIRES_QUESTION.lower() == "yes":
            install_requires = input("Packages to install (comma-separated): ").split(",")
        KEYWORDS_QUESTION = input("\nWould you like to provide keywords? (y/n): ")
        if KEYWORDS_QUESTION.lower() == "y" or KEYWORDS_QUESTION.lower() == "yes":
            keywords = input("Keywords (comma-separated): ").split(",")
        CLASSIFIERS_QUESTION = input("\nWould you like to provide classifiers? (y/n): ")
        if CLASSIFIERS_QUESTION.lower() == "y" or CLASSIFIERS_QUESTION.lower() == "yes":
            classifiers = input("Classifiers (comma-separated): ").split(",")
        PYTHON_REQUIRES_QUESTION = input("\nWould you like to provide a minimum Python version? (y/n): ")
        if PYTHON_REQUIRES_QUESTION.lower() == "y" or PYTHON_REQUIRES_QUESTION.lower() == "yes":
            python_requires = input("Minimum Python Version: ")

    # Creating setup.py text (yes this is just the whole setup.py file in a list)
    setup_file =[
        "from setuptools import setup, find_packages\n",
        "from os.path import dirname, join, isfile\n",
        "readme_exists = True\n",
        "long_description = \"\"",
        "\n\n# Get the long description from the README file if it exists\n",
        "if isfile(join(dirname(__file__), \"README.md\")):\n",
        "\tREADME_PATH = join(dirname(__file__), \"README.md\")\n",
        "elif isfile(join(dirname(__file__), \"docs/README.md\")):\n",
        "\tREADME_PATH = join(dirname(__file__), \"docs/README.md\")\n",
        "else:\n",
        "\treadme_exists = False\n",
        "\n# Get the long description from the README file if it exists\n",
        "if readme_exists:\n",
        "\twith open(README_PATH) as file:\n",
        "\t\tlong_description = file.read()\n",
        "\nsetup(\n",
        "\tname = \"" + NAME + "\",\n",
        "\tversion = \"" + VERSION + "\",\n",
        "\tauthor = \"" + AUTHOR + "\",\n",
        "\tdescription = \"" + DESCRIPTION + "\",\n",
        "\tlong_description = long_description,\n",
        f"\tlong_description_content_type = \"{long_description_content_type}\",\n"
        "\tpackages = find_packages()",
    ]
    if url:
        setup_file.append(",\n\turl = \"" + url + "\"")
    if install_requires:
        setup_file.append(",\n\tinstall_requires = " + str(install_requires).lower().replace(" ", ""))
    if keywords:
        # Remove the first character of each keyword if it is a space
        for i, KEYWORD in enumerate(keywords):
            if KEYWORD[0] == " ":
                keywords[i] = KEYWORD[1:]
        setup_file.append(",\n\tkeywords = " + str(keywords).replace(" ", ""))
    if classifiers:
        # Remove the first character of each classifier if it is a space
        for i, CLASSIFIER in enumerate(classifiers):
            if CLASSIFIER[0] == " ":
                classifiers[i] = CLASSIFIER[1:]
        setup_file.append(",\n\tclassifiers = " + str(classifiers))
    if python_requires:
        setup_file.append(",\n\tpython_requires = \"" + python_requires + "\"")
    setup_file.append("\n)")

    # Writing setup.py file
    with open(FILE_PATH, "w") as file:
        for line in setup_file:
            file.write(line)

    print("\nsetup.py file created!\n")
    return True
    

if __name__ == "__main__":
    create_setup()