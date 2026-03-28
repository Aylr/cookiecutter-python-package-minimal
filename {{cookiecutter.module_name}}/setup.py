# !/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

with open("requirements.txt") as f:
    required = [line for line in f.read().splitlines() if not line.startswith("#")]

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="{{cookiecutter.module_name}}",
    packages=find_packages(),
    version="0.0.1",
    description="{{cookiecutter.short_description}}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="{{cookiecutter.author}}",
    url="{{cookiecutter.repo_url}}",
    keywords=[""],
    install_requires=required,
    scripts=[],
    include_package_data=True,
)
