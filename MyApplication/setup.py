from distutils.core import setup

setup(
	#Application Name
	name="MyApplication", 

	#Version Number (Initial)
	version=0.1.0,

	#Aplication Author Details
	author="name surname",
	author_email="name@addr.ess",

	#Packages
	packages=["app"],

	#Include Aditional Files into the Package
	include_package_data=True,

	#Details
	url="http://pypi.python.org/pypi/MyApplication_v010/",

	#License
	license=LICENSE.txt,
	
	description="Useful towel-related stuff.",

	long_description=open("README.txt").read(),

	#Dependencies
	install_requires=[
		"Flask",
		],

	)