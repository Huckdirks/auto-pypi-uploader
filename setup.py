from setuptools import setup, find_packages
from os.path import dirname, join, isfile

readme_exists = True
long_description = ""

# Get the long description from the README file if it exists
if isfile(join(dirname(__file__), "README.md")):
    README_PATH = join(dirname(__file__), "README.md")
elif isfile(join(dirname(__file__), "docs/README.md")):
    README_PATH = join(dirname(__file__), "docs/README.md")
else:
    readme_exists = False

# Set the long description if the README file exists
if readme_exists:
    with open(README_PATH, "r") as file:
        long_description = file.read()

setup(
    name = "auto_pypi_uploader",
	version = "1.1.1.3",
    author = "Huck Dirksmeier",
    author_email = "Huckdirks@gmail.com",
    description = "A program to automate the creation of the 'setup.py' file, changing a pip package's version, & publishing it to PyPi.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    license = "MIT",
    url = "https://github.com/Huckdirks/auto-pypi-exporter",
    packages = find_packages(),
    install_requires = ["python-dotenv", "twine", "wheel", "setuptools"],
    keywords = ["PyPi", "Pip", "setup", "setup.py", "automation"],
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = ">=3.0"
)