from setuptools import setup, find_packages

setup(
    name="cf_helper",  
    version="0.2.2",  
    description="A Python library for interacting with Codeforces API and automating tasks.",
    long_description=open("README.md").read(),  
    long_description_content_type="text/markdown",
    author="Shubham Kumar Verma",
    author_email="skv.iitroorkee@gmail.com",
    url="https://github.com/skv-1180/CF-Automate",
    packages=find_packages(), 
    install_requires=[
        "requests", 
        "python-dotenv==0.20.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
