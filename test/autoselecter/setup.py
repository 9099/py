#encding :utf-8
from setuptools import setup,find_packages
setup(
	name='autoselecter',
	version='1.0',
	packages=['autoselecter'],
	entry_points={
		'console_scripts':[
			'auto = autoselecter.__main__:main'
		]
	},
	install_requires=[
		'requests'
	]

)