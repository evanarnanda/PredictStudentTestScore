from setuptools import find_packages, setup
from typing import List


def get_requirements(file: str) -> List[str]:
    '''
    this function for returning list of requirements
    '''
    reqs = []
    with open(file) as file_obj:
        reqs = file_obj.readlines()
        reqs = [req.replace('\n', '') for req in reqs]

    if '-e .' in reqs:
        reqs.remove('-e .')

    return reqs


setup(
    name='mlproject',
    version='0.0.1',
    author='Evan Arnanda',
    author_email='evanarnanda@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
