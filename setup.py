try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import io
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with io.open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

install_requires = [
    'jupyter>=1.0.0',
]

setup(
    name='inumpy',
    version='0.0.1',
    description='Numpy extension for IPython',
    long_description=long_description,
    url='https://github.com/piti118/inumpy',

    # Author details
    author='Piti Ongmongkolkul',
    author_email='',

    # Choose your license
    license='',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Topic :: Text Processing :: Markup :: HTML',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    # What does your project relate to?
    keywords='ipython jupyter notebook numpy',

    py_modules=['inumpy'],
    install_requires=install_requires,
)
