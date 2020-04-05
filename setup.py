import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="parsehub-client",
    version="0.0.1",
    description="ParseHub API client",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/ebragas/parsehub-client",
    author="Eric Bragas",
    author_email="ericbragas412@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=("tests",)),
    install_requires=["requests"],
)