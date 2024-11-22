from setuptools import setup, find_packages

setup(
    name="json-column-processor",
    version="0.1.0",
    description="A Python library to process DataFrames with nested JSON columns.",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/json-column-processor",
    packages=find_packages(),
    install_requires=[
        "pandas",
    ],
    python_requires=">=3.12",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
