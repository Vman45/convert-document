from setuptools import setup, find_packages

setup(
    name='convert',
    version='1.3.0',
    packages=find_packages(exclude=[]),
    install_requires=[
        'aiohttp',
        'pantomime',
        'pyicu'
    ],
)
