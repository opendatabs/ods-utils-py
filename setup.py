from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements_list = f.read().splitlines()

with open("LICENSE") as f:
    license_text = f.read()

with open("README.md", "r") as f:
    readme_text = f.read()

setup(
    name="ods_utils_py",
    version="0.1.0",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    description="A Python package for interacting with OpenDataSoft (ODS) platforms.",
    author="Rstam ALOUSH",
    author_email="rstam.aloush@bs.ch",
    install_requires=requirements_list,
    license=license_text,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
    long_description=readme_text,
    long_description_content_type="text/markdown",
    #url='https://github.com/rstam-aloush/odsAutomationPython/'
)
