from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="haiku",
    version="0.1.0",
    author="Hitesh Regar",
    author_email="haikent.work@gmail.com",
    description="A command-line interface for interacting with Ollama AI models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/haiku",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/haiku/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Utilities",
    ],
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=["ollama", "rich"],
    entry_points={
        "console_scripts": [
            "haiku=src.main:main",
        ],
    },
)