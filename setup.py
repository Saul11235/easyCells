from setuptools import setup, find_packages

setup(
    name='easyCells',         
    version='0.0.1', 
    description='simple python package for easy use with XlsxWriter',
    author='Edwin Saul',
    author_email='edwinsaulpm@gmail.com',
    packages=find_packages(),  # Automatically discover and include all packages
    keywords='XlsxWriter xlsx document',
    install_requires=[
        "XlsxWriter"
    ],
)
