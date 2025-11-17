#Setup replated code: Packaging the ML project as a Python library | Facilitating installation and deployment: | Managing project structure and distribution
from setuptools import find_packages, setup

setup(
    name= "Ml_pipeline",
    version = "0.0.0",
    author = "Nandini",
    author_email = "nandiniraghav16@gmail.com",
    packages = find_packages(),
    install_requires=[]
)