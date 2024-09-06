import os

from setuptools import setup

with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md")) as f:
    README = f.read()

setup(
    name="statsbombpy",
    version="1.14.0",
    description="easily stream StatsBomb data into Python",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/statsbomb/statsbombpy",
    author="StatsBomb",
    author_email="support@statsbombservices.com",
    packages=["statsbombpy"],
    install_requires=[
        "pandas",
        "requests",
        "requests-cache",
        "inflect",
        "joblib",
    ],
    extras_require={
        'dev': [
            "nose2",
        ]
    },
)
