# Auto Pip Exporter

## Table of Contents

- [Introduction](#introduction)
- [Uses](#uses)
    - [Running from Command Line](#running-from-command-line)
    - [Running with Command Line Arguments](#running-with-command-line-arguments)
    - [Importing as a Module](#importing-as-a-module)
        - [`pypi_exporter()`](#pypi_exporter-takes-in)
        - [`setup_env()`](#setup_env-takes-in)
- [Running](#running)
    - [Dependencies](#dependencies)
    - [Setting Up .env File](#setting-up-env-file-1)
    - [Running](#running-1)
- [Quality Assurance](#quality-assurance)
- [Suggestions](#suggestions)
- [Contributing](#contributing)
- [License](#license)

## Introduction

While working on my previous project: [text-excuse-generator](https://github.com/Huckdirks/text-excuse-generator), I just published my first package to [PyPi](https://pypi.org/project/text-excuse-generator/). I quickly realized that I wasn't going to be able to remember the command line arguments to pass into the required fields, and that I was bound to forget to change the version manually in the `setup.py` file every time I updated the package. So I decided to make a program that would automatically update the version number in the `setup.py` file and export my project to PyPi.

## Uses

There are three main ways to interact with the program: by running it normally, by running it with command line arguments, or by importing it into another python file.

### Running from Command Line

I'd recommend just downloading [excuse_generator.py](../text_excuse_generator/excuse_generator.py) and running it from the command line. You can run it by typing:
```bash
python3 text_excuse_generator.py
```
If you just want the [excuse_generator.py](../text_excuse_generator/excuse_generator.py) file for a project, please also include the [LICENSE](../LICENSE) file in the same directory as [excuse_generator.py](../text_excuse_generator/excuse_generator.py).

When you run the program normally, it will ask you for the sender, recipient, problem, and excuse, and if you want to send the text message. It will then generate a text message, and send it to the recipient if chosen. If you input a name into recipient that isn't saved to the system yet when sending a text, it will ask you if you want to save it to the system. If you choose to save it, it will ask you for the phone number, and then save it to the system. You can also just use a phone number for the recipient field, and it will send the text to that number.

### Running with Command Line Arguments

You can also run the program with command line arguments. If you want to send the text message, you can add `--send` or `-s` as the last argument. All command line arguments longer than a single word need to be in parentheses. I'd recommend just downloading [excuse_generator.py](../text_excuse_generator/excuse_generator.py) and running it from the command line. If you just want the [excuse_generator.py](../text_excuse_generator/excuse_generator.py) file for a project, please also include the [LICENSE](../LICENSE) file in the same directory as [excuse_generator.py](../text_excuse_generator/excuse_generator.py).

#### **Sending a Text Message**

If you want to send a text with command line arguments, run:
```bash
python3 text_excuse_generator.py [sender] [recipient] [problem] [excuse] [--send_text_flag]
```
e.g.
```bash
python3 text_excuse_generator.py Me "Your mom" "I'm late to 😈" "Too many wizards around" -s
```
Omit the `[--send_text_flag]` if you don't want to send the text message.

#### **Setting Up .env File**
If you want to set up the .env file, run:
```bash
python3 text_excuse_generator.py [-e/--setup_env] [TWILIO_ACCOUNT_SID] [TWILIO_AUTH_TOKEN] [TWILIO_PHONE_NUMBER] [OPENAI_API_KEY]
```
e.g.
```bash
python3 text_excuse_generator.py -e "AC1234567890" "1234567890" "+15555555555" "sk-1234567890"
```

#### **Saving a New Recipient**

If you want to save a new recipient to the system, run:
```bash
python3 text_excuse_generator.py [-a/--add] [name] [phone_number]
```
e.g.
```bash
python3 text_excuse_generator.py -a "Your mom" +15555555555
```

### Importing as a Module

You can also import the program as a module into another python file. The `text_excuse_generator` module has  four functions: `generate_excuse()`, `setup_env()`, `add_recipient()`, & `send_twilio_text()`.

#### Installing with pip

Simply run:
```bash
pip install text-excuse-generator
```
To import the module into your python file, put this at the top of your file:
```python
from text_excuse_generator.excuse_generator import *
```
Or you can import the individual functions.

#### `generate_excuse()` takes in:
```python
generate_excuse(USER: str, RECIPIENT: str, PROBLEM: str, EXCUSE: str, SEND_TEXT: bool) -> str
```
`generate_excuse()` returns a string of the text message that was generated.

If you want to generate a text message, call the function like this:

```python
generate_excuse("user", "recipient", "problem", "excuse", True)
```
e.g.
```python
generate_excuse(user = "me", recipient = "your mom", problem = "I'm late to 😈", excuse = "Too many wizards around", send_text = True)
```
Make sure to put the fields before the variables when calling the function. Omit the `[--send_text_flag]` if you don't want to send the text message.

#### `setup_env()` takes in:
```python
setup_env(TWILIO_ACCOUNT_SID: str, TWILIO_AUTH_TOKEN: str, TWILIO_PHONE_NUMBER: str, OPENAI_API_KEY: str) -> bool
```
If you want to set up your .env file, call `setup_env()` like this:
```python
setup_env("TWILIO_ACCOUNT_SID", "TWILIO_AUTH_TOKEN", "TWILIO_PHONE_NUMBER", "OPENAI_API_KEY")
```
e.g.
```python
setup_env("AC1234567890abcdef1234567890abcdef", "1234567890abcdef1234567890abcdef", "+15555555555", "sk-1234567890")
```
`setup_env()` returns True if the .env file was successfully set up, and False if it wasn't (Invalid phone number).

#### `add_recipient()` takes in:
```python
add_recipient(NAME: str, PHONE_NUMBER: str) -> bool
```
If you want to save a new recipient to the system, call `add_recipient()` like this:
```python
add_recipient("new_recipient_name", "new_recipient_phone_number")
```
e.g.
```python
add_recipient("Your Mom", "+15555555555")
```
`add_recipient()` returns True if the recipient was successfully added to the system, and False if it wasn't (Invalid phone number or phone number is already in the system).

#### `send_twilio_text()` takes in:
```python
send_twilio_text(RECIPIENT_PHONE_NUMBER: str, MESSAGE: str) -> None
```
If you want to send a text message, call `send_twilio_text()` like this:
```python
send_twilio_text("recipient_phone_number", "message")
```
e.g.
```python
send_twilio_text("+15555555555", "Beep boop beep bop")
```

## Running

### Dependencies

#### Accounts

You'll need to create a [PyPi](https://pypi.org/account/register/) account. Once you get your account set up, you'll need to [set up the `.env` file](#setting-up-env-file-1) with this information:
- Username
- Password

#### Install Dependencies

Double click [`dependencies`](../dependencies), or run `bash `[`dependencies`](../dependencies) or `./`[`dependencies`](../dependencies) in the command line in the root directory to install the python dependencies. You must have [pip](https://pip.pypa.io/en/stable/installation/) installed to download the new dependencies. Also, you'll need to install [python](https://www.python.org/downloads/) yourself if you haven't already.

**[List of Dependencies](DEPENDENCIES.md)**

### Setting Up .env File

Either run the program without any arguments to manually input the information for the .env file, run with [command line arguments](#setting-up-env-file) to automatically input the information for the .env file, or pass in the correct parameters to the [`setup_env()`](#setup_env-takes-in) function.

### Running

**YOU HAVE TO INSTALL THE DEPENDENCIES & SETUP THE `.env` FILE BEFORE TRYING TO RUN THE PROGRAM!!!**

Run `python3 text_excuse_generator.py` or `python3 text_excuse_generator.py [sender] [recipient] [problem] [excuse] [--send_text_flag]` in the command line in the source directory.

More detailed instructions are in the [Uses](#uses) section.

## Quality Assurance
All variable, function, class, module, & file names are written in [snake_case](https://en.wikipedia.org/wiki/Snake_case) to make sure everything is consistent, and all `const` variables are written in ALL-CAPS. The code is also quite commented and the variable names are quite verbose, so it should be easy enough to understand what's going on.

If there are any other/better ways to check for quality assurance, please let me know in the [suggestions](https://github.com/Huckdirks/auto-pip-exporter/discussions/new?category=suggestions)!

## Suggestions

If you have any suggestions about anything, please create a [new discussion in suggestions](https://github.com/Huckdirks/auto-pip-exporter/discussions/new?category=suggestions).

## Contributing

Contributions are always welcomed! Look at [CONTRIBUTING.md](CONTRIBUTING.md) for more information.

## License

The project is available under the [MIT](https://opensource.org/licenses/MIT) license.
