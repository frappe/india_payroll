from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in india_payroll/__init__.py
from india_payroll import __version__ as version

setup(
	name="india_payroll",
	version=version,
	description="India Compliance Payroll",
	author="Frappe Technologies Pvt Ltd",
	author_email="developers@frappe.io",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
