from setuptools import setup

from python_repo_template import __version__

with open("README.md", mode="r", encoding="utf-8") as fp:
    long_description = fp.read()


setup(
    name="python-repo-template",
    version=__version__,
    description="GitHub Template for Python Repositories.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Dani El-Ayyass",
    author_email="dayyass@yandex.ru",
    license_files=["LICENSE"],
    url="https://github.com/dayyass/python-repo-template",
    packages=["python_repo_template"],
)
