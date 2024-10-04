# Developer Guide for `ods_utils_py`

This guide provides instructions on setting up the development environment, adding new functions, and contributing code to this repository.

## Table of Contents
- [Getting Started](#getting-started)
- [Setting Up the Development Environment](#setting-up-the-development-environment)
- [Installation Instructions](#installation-instructions)
- [Adding New Functions](#adding-new-functions)
- [Commit Message Guidelines](#commit-message-guidelines)
- [License](#license)

---

## Getting Started

1. **Clone the Repository**
   ```bash
   git clone https://github.com/rstam-aloush/ods-utils-py.git
   ```

2. **Change to the Project Directory**
   ```bash
   cd ods-utils-py
   ```

3. **Set Up Environment Variables**
   Copy your [`.env.template`](.env.template) and rename it to `.env`:
   - **Windows**
     ```cmd
     copy .env.template .env
     ```
   - **Mac/Linux**
     ```bash
     cp .env.template .env
     ```
   Open the `.env` file and fill in your credentials and other required information.

---

## Setting Up the Development Environment

It is recommended to create and use a virtual environment for local development. Follow the steps below to set up the environment based on your operating system:

4. **Create Virtual Environment**
   ```bash
   python -m venv .venv
   ```

1. **Activate Virtual Environment**

   - **Windows**
     ```bash
     .venv\Scripts\activate
     ```

   - **Mac/Linux**
     ```bash
     source .venv/bin/activate
     ```

1. **Install Required Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

**Make sure to:** 
- activate the virtual environment before running ```pip``` commands 
- run python from 
```./.venv/Scripts/python.exe``` in IDEs.

This will install all the necessary dependencies for local development.

---

## Installation Instructions

To install the package in a separate folder for testing purposes, run:

```bash
pip install -e <path/to/this/folder>
```

Using the `-e` (editable) flag ensures that the package needs to be installed only once and remains up-to-date with the version that is currently loaded from the source folder.

---

## Adding New Functions

When adding a new function to the package, use the following steps to ensure consistency across the codebase:

1. Copy the template file: `get_number_of_datasets.py`.
2. Follow the structure and code style present in the template when implementing the new function.
3. Document the function with clear and concise docstrings following standard Python conventions (e.g., describing arguments, return values, and any exceptions raised) **where deemed necessary**.

---

## Commit Message Guidelines

Commit messages should be meaningful and follow a clear format. Each commit message should complete the sentence:

> "When applied, this commit will ..."

### Guidelines:
- **Start with an uppercase letter**.
- **Do not end with a period**.
- Be **concise** and **descriptive**.

#### Examples:
- `Update README_FOR_DEVELOPERS.md`
- `Add new function get_number_of_datasets`

This format helps maintain clarity and readability in the commit history.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file in the repository for the full license text.
