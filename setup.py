from setuptools import setup, find_packages

setup(
    name="haiku",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["ollama", "rich"],
    entry_points={
        "console_scripts": [
            "haiku=src.main:main",
        ],
    },
)