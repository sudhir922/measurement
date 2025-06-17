try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'measurement',
    'author': 'Sudhir Sahu',
    'url': 'https://github.com/sudhir922/measurement',
    'download_url': 'https://github.com/sudhir922/measurement',
    'author_email': 'sudhir922@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['measurement'],
    'scripts': [],
    'name': 'measurement'
}

setup(**config)