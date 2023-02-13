from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in from_bank/__init__.py
from from_bank import __version__ as version

setup(
	name="from_bank",
	version=version,
	description="this App is to manage external loans from banks ",
	author="Ahmed Fourati",
	author_email="ahmed.fourati@slnee.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
