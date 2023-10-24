#
from os import system

system("pip uninstall easyCells")
system("python setup.py sdist bdist_wheel")
system("pip install .")
