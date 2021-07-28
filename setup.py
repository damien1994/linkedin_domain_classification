from setuptools import setup

setup(
    name='job_title_classificator',
    author='Damien Michelle',
    author_email='damienmichelle1994@hotmail.com',
    version='1.0',
    packages=['domain_classification'],
    include_package_data=True,
    python_requires='~=3.7',
    description='Classify job titles as Tech job or not',
    license='LICENSE',
    entry_points={
        'console_scripts': ['domain_classification=domain_classification.main:main']
    },
    long_description=open('README.md').read()
)
