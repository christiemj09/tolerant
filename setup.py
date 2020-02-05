"""
Install tolerant.
"""

def main():
	try:
		from setuptools import setup
	except ImportError:
		from distutils.core import setup

	config = {
		'description': 'Wrap functions in error-tolerant response objects.',
		'author': 'Matt Christie',
		'download_url': 'https://github.com/christiemj09/pyskeleton',
		'author_email': 'christiemj09@gmail.com',
		'version': '0.1',
		'install_requires': [],
		'packages': ['tolerant'],
		'scripts': [],
		'entry_points': {
		    'console_scripts': [],
		},
		'name': 'tolerant',
	}

	setup(**config)	

if __name__ == '__main__':
	main()

