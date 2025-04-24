from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements_list = f.read().splitlines()

with open("LICENSE") as f:
    license_text = f.read()

with open("README.md", "r") as f:
    readme_text = f.read()

setup(
    name="ods_utils_py",
    version="0.1.22",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    description="A python wrapper library for the ODS Automation API",
    author="Renato FARRUGGIO",
    author_email="renato.farruggio@bs.ch",
    install_requires=requirements_list,
    license=license_text,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
    long_description=readme_text,
    long_description_content_type="text/markdown",
    url='https://github.com/opendatasoft/ods-utils-py/'
)
