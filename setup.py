from setuptools import setup, find_packages

setup(
    name='SteamApiAccessor',
    version='1.0',
    description='A module to access the public Steam API with some helpful methods to manipulate the returned request',
    author='Eli Corpron',
    packages=find_packages(),  # same as name
    install_requires=['requests'],  # external packages as dependencies
)
