import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '1.0.3'
PACKAGE_NAME = 'borders'
AUTHOR = 'Simon Calvaruso'
AUTHOR_EMAIL = 'calvaruso.simone@gmail.com'
URL = 'https://github.com/scalvaruso/borders'

LICENSE = 'MIT License'
DESCRIPTION = 'A module to create a frame when printing a list of strings.'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages()
      )