from setuptools import setup


setup(
    name="statsbombpy",
    version="1.0",
    description="easily stream StatsBomb data into Python",
    long_description="easily stream StatsBomb data into Python",
    url="https://github.com/statsbomb/statsbombpy",
    author="StatsBomb",
    author_email="support@statsbombservices.com",
    packages=["statsbombpy"],
    install_requires=["cashier", "inflect", "nose2", "pandas", "requests", "requests-cache"],
)
