# Developer Guide for `ods_utils_py`

This guide provides instructions on setting up the development environment, adding new functions, and contributing code to this repository.

## Table of Contents
- [Getting Started](#getting-started)
- [Setting Up the Development Environment](#setting-up-the-development-environment)
- [Installation Instructions](#installation-instructions)
- [Adding New Functions](#adding-new-functions)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Function Naming Conventions](#function-naming-conventions)

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

3. **Ensure You Are on the `develop` Branch**
   ```bash
   git checkout develop
   ```

   *Note:* If `develop` is already the default branch, you are already on it after cloning. This step ensures you are on the correct branch if multiple branches exist.
   
   **IMPORTANT:** Never push directly to the `main` branch!

4. **Set Up Environment Variables**
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

5. **Create Virtual Environment**
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

To install the package for testing purposes, run:

```bash
pip install -e .
```

Using the `-e` (editable) flag ensures that the package needs to be installed only once via pip and remains up-to-date with the current version in the source folder.

---

## Adding New Functions

When adding a new function to the package, use the following steps to ensure consistency across the codebase:

1. Copy the template file: `src/ods_utils_py/get_number_of_datasets.py`.
2. Follow the structure and code style present in the template when implementing the new function.
3. Document the function with clear and concise docstrings following standard Python conventions (e.g., describing arguments, return values, and any exceptions raised) **where deemed necessary**.
Add unit tests. Check out the file `tests/test_get_number_of_datasets.py` as a reference.

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

## Function Naming Conventions

As our project grows, we may introduce specific naming conventions for functions to ensure consistency and improve code navigation. Currently, we don't have strict rules, but we recommend following these general guidelines:

1. Use lowercase letters and underscores for function names (snake_case).
2. Choose descriptive names that clearly indicate the function's purpose.
3. Prefer verb-noun combinations for action-oriented functions.

Examples of good function names:
- `get_dataset_info`
- `calculate_average_score`
- `validate_user_input`

We may introduce more specific conventions in the future, such as prefixes or suffixes for certain types of functions. As these conventions are established, they will be documented here.

**Note:** This section will be updated with more detailed conventions as the project evolves and requires additional structure.

---
