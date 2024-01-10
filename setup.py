from setuptools import setup

setup(
    name='passg',
    version='1.0.0',
    py_modules=['passg'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'passg = passg:cli',
        ],
    },
)