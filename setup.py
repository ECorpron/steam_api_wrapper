from setuptools import setup

setup(
    name='steam_api_wrapper',
    version='0.3',
    description='A module to access the public Steam API with some helpful methods to manipulate the returned request',
    author='Eli Corpron',
    packages=['steam_api_wrapper'],
    install_requires=['requests'],  # external packages as dependencies
)
