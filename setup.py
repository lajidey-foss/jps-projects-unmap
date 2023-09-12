from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in jpsage_projects_idea/__init__.py
from jpsage_projects_idea import __version__ as version

setup(
	name="jpsage_projects_idea",
	version=version,
	description="Simple idea tracker to enable project ideas are follow through foretter ",
	author="Jide Olayinka and all Ardentpros contributors",
	author_email="spryngmanaged@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
