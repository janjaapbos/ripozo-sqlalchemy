from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from setuptools import setup, find_packages


version = '0.1.5.dev0'

setup(
    name='ripozo-sqlalchemy',
    version=version,
    packages=find_packages(exclude=['tests', 'tests.*']),
    url='',
    license='',
    author='Tim Martin',
    author_email='tim.martin@vertical-knowledge.com',
    description=('Integrates SQLAlchemy with ripozo to'
                 ' easily create cassandra backed Hypermedia/HATEOAS/REST apis'),
    install_requires=['ripozo', 'SQLAlchemy'],
    tests_require=['tox', 'ripozo-tests', 'mock'],
    test_suite="ripozo_sqlalchemy_tests",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)