'''Configures uil_psychopy'''

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

# The directory where this file is located.
uil_psychopy_dir = path.abspath(path.dirname(__file__))

short_description = "UiL OTS psychopy utilities"

upp_deps = ['psychopy', 'pygobject']

setup(name="uil_psychopy",
      version="0.0.0",
      description=short_description,
      license="GPL-3.0",
      url="https://github.com/UiL-OTS-labs/uil_psychopy",
      author="Maarten Duijndam",
      classifiers=[
        'Development Status :: 3',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
      ],
      packages=find_packages(),
      install_requires=['psychopy', '']
      )


