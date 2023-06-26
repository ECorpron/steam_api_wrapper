from setuptools import setup, find_packages

setup(
    name='SteamApiAccessor',
    version='0.1.1',
    description='A module to access the public Steam API with some helpful methods to manipulate the returned request',
    author='Eli Corpron',
    packages=['steam_api_accessor'],  # same as name
    install_requires=['requests'],  # external packages as dependencies
)
