from setuptools import setup, find_packages
from typing import List


# Declaration Variable for setup function
PROJECT_NAME = "insurance-fraud-predector"
VERSION = "0.0.1"
DESCRIPTION = ""
AUTHOR = "Ved Prakash Sharma"
AUTHER_EMAIL = "vedprakashjangid.jpr@gmail.com"
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: this function is going to return a list of requirement 
    mention in requirements.txt file.
    
    Return: this function is going to return a list which contain name of 
    library of requirement mention in requirements.txt file.
    """
    with open(REQUIREMENT_FILE_NAME, 'r') as requirement_txt:
        return requirement_txt.readlines().remove('-e .')

setup(
    name= PROJECT_NAME,
    version= VERSION,
    description= DESCRIPTION,
    author= AUTHOR,
    author_email= AUTHER_EMAIL,
    packages= find_packages(),
    install_requires= get_requirements_list()
    
)