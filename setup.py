from setuptools import setup

setup(
    name='bujo',
    version='0.0.1',
    py_modules=['bujo'],
    install_requires=['Click', 'TinyDB', 'tqdm'],
    entry_points='''
        [console_scripts]
        bujo=bujo:cli
    '''
        )
