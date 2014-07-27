from setuptools import setup, find_packages


setup(
    name='pygenus',
    version='0.1.0',
    packages=find_packages(),
    author='Emil Stenqvist and Janis Abele',
    description='A work-in-progress Python module for identifying mentions of'
                'gender in text using natural language processing.',
    entry_points={
        'console_scripts': [
            'pygenus=pygenus:main',
        ],
    },
)
