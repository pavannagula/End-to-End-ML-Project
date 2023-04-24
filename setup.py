from setuptools import setup, find_packages
from .venv.Lib.typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    ### this function will read the requirements file and return a list of requirements##

    requiremnets = []
    with open(file_path, 'r') as f:
        requiremnets = f.read().readlines()
        requiremnets = [x.strip() for x in requiremnets]

        if HYPEN_E_DOT in requiremnets:
            requiremnets.remove(HYPEN_E_DOT)
    return requiremnets


setup(
    name = 'MLproject',
    version= '0.0.1',
    author='Pavan',
    author_email='npavankumar36@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)