
from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #reading lines from file
            lines = file.readlines()
            #process each line
            for line in lines:
                requirement=line.strip()
                ## ignore the lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
                    
    except FileNotFoundError:
        print("requirements.txt is not found")
        
    return requirement_lst

setup(
    name = "NetworkSecuirty",
    version="0.0.1",
    author = "NikhilNellutla",
    author_email="nikhilnellutla55@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
    
)
