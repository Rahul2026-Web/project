# from setuptools import find_packages,Setup
# from typing import List


# def get_requirements(file_path:str)->List[str]:

#     requirements=[]
#     with open (file_path) as file_obj:
#         requirements=file_obj.readlines()
#         requirements=[req.replace("\n","") for req in requirements]


# setup(
#     name='mlproject',
#     version='0.0.1',
#     author='Rahul Yadav',
#     author_email='rahulbhai7320021gmail.com',
#     packages=find_packages(),
#     install_requires=get_requirements('requirements.txt')
# )





from setuptools import find_packages, setup  # Fixed `Setup` to `setup`
from typing import List

HYPEN_E_DOT='-e .' 
def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and req.strip() != "-e ."]
    
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)


    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Rahul Yadav',
    author_email='rahulbhai7320021@gmail.com',  # Fixed email syntax
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
