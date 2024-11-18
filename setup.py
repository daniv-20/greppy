from setuptools import setup, find_packages

setup(
    name="greppy",
    version="0.1.0",
    description="A simple grep-like functionality for Python.",
    author="DJV",
    author_email="dvait16@gmail.com",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
