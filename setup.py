
from distutils.core import setup
import sys

sys.path.append('math_util')
import prime_factors


setup(name='prime_factors',
            version='1.0',
            author='Abhinav Jauhri',
            author_email='abhinav.jauhri@gmail.com',
            url='https://github.com/aj910martin/math_util',
            download_url='https://github.com/aj910martin/math_util',
            description='Print prime factors in Python',
            long_description=prime_factors.__doc__,
            package_dir={'': 'math_util'},
            py_modules=['prime_factors','prime_numbers'],
            provides=['prime_factors','prime_numbers'],
            keywords='prime sieve factors',
            license='GNU LESSER GENERAL PUBLIC LICENSE v3',
            classifiers=['Development Status :: 5 - Production/Stable',
                         'Intended Audience :: Developers',
                         'Natural Language :: English',
                         'Operating System :: OS Independent',
                         'Programming Language :: Python :: 2.7',
                         'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
                         'License :: OSI Approved :: GNU Affero General Public License v3',
                         'Topic :: Utilities',
                        ],
           )
