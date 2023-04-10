# Python Libraries
from os import getcwd, system
from os.path import dirname, join, isfile
from sys import argv

# Constants
FILE_NAME = "setup.py" 
FILE_PATH = getcwd() + "/" + FILE_NAME


# Create a setup.py file
def setup_file_creator(**kwargs) -> bool:
    if kwargs and (not kwargs["name"] or not kwargs["version"] or not kwargs["author"] or not kwargs["description"]):
        print("Please provide the minimum required parameters: name, version, author, & description\ne.g. setup_file_creator(name=\"auto-pypi-exporter\", version=\"1.0.0\", author=\"Huck Dirksmeier\", description=\"A program to automate changing a pip package's version & publishing it\")")
        return False
    elif len(argv) > 1 and len(argv) < 5:
        if argv[1].lower() == "-h" or argv[1].lower() == "--help":  # Give info on how to use the program here
            system("clear")
            print("This program has four required parameters: name, version, author, & description")
            print("You can provide these parameters in one of two ways:")
            print("\t1. As command line arguments")
            print("\t\Usage: python setup_file_creator.py [-n/--name] NAME [-v/--version] \"0.0.0\" [-a/--author] \"AUTHOR\" [-d/--description] \"DESCRIPTION\"")
            print("\t2. As parameters in a function call")
            print("\t\Usage: setup_file_creator(name=\"NAME\", version=\"0.0.0\", author=\"AUTHOR\", description=\"DESCRIPTION\")\n")
            print("It can also take some optional parameters:")
            print("\t1. -h or --help: This help message")
            print("\t2. -l or --long_description_content_type: The long description type of the package (default: \"text/markdown\")")
            print("\t3. -u or --url: The URL to the website or GitHub repository for the project")
            print("\t4. -i or --install_requires: The necessary packages to install for the package to work")
            print("\t\tMust be in a comma-separated list WITHOUT SPACES!!!")

            print("If you do not provide any parameters, the program will ask you for them")
            print("The program will automatically create a setup.py file in the current directory if one is not found")

        print("Please provide the minimum required parameters: name, version, author, & description\ne.g. setup_file_creator(name=\"auto-pypi-exporter\", version=\"1.0.0\", author=\"Huck Dirksmeier\", description=\"A program to automate changing a pip package's version & publishing it\")")
        return False
    

if __name__ == "__main__":
    setup_file_creator()