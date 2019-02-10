
from setuptools import setup

setup(
    name="{{cookiecutter.app_name}}",
    version="1.0",
    packages=["{{cookiecutter.app_name}}"],
    include_package_data=True,
    install_requires=[
        'Flask'
    ]
)
