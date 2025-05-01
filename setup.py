from setuptools import find_packages, setup

_PACKAGE_VERSION = "0.1.0"

with open("README.md", "r", encoding="utf-8") as md:
    long_description = md.read()

with open("requirements.txt", "r") as txt:
    requirements = [line.strip() for line in txt.readlines()]

with open("LICENSE", "r") as license_file:
    license_content = license_file.read()

setup(
    name="demo_package",
    version=_PACKAGE_VERSION,
    author="Edmond Makolle",
    author_email="edghimakoll@gmail.com",
    description="Demo package for Python packaging",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Edmond22-prog/demo-package",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=[requirements],
    license=license_content,
)
