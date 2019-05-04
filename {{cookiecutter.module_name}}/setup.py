# !/usr/bin/env python

from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="{{cookiecutter.module_name}}",
    packages=["{{cookiecutter.module_name}}"],
    version="0.0.1",
    description="{{cookiecutter.short_description}}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="{{cookiecutter.author}}",
    url="{{cookiecutter.repo_url}}",
    keywords=[""],
    install_requires=[],
    scripts=[],
    include_package_data=True,
)
