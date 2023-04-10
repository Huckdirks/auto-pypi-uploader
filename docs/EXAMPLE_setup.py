from setuptools import setup, find_packages
from os.path import dirname, join

# Get the long description from the README file
README_PATH = join(dirname(__file__), "docs/README.md")

with open(README_PATH, "r") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name = "PROGRAM NAME",
	version = '0.0.0',
    author = "YOUR NAME",
    author_email = "YOUR_EMAIL@gmail.com",
    description = "DESCRIPTION",
    long_description = LONG_DESCRIPTION,
    long_description_content_type = "text/markdown",
    packages = find_packages(),
    install_requires = ["LIST", "OF", "PIP", "PACKAGES", "HERE"],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = ">=3.8"
)