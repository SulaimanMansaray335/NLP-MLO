from setuptools import find_packages, setup
from typing import List


def get_requirements() -> List[str]:

    requirements_list:List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement != 'e- .':
                    requirements_list.append(requirement)            
    except FileNotFoundError as e:
        print("requirements.txt not found")
    return requirements_list 


setup(
    name = 'NLP_MLO_Project',
    version = '0.0.1',
    author_email = 'Tariq.Mansaray@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements()
)