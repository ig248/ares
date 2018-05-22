from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

VERSION = '0.0.1'

# List your project dependencies here.
# For more details, see:
# http://packages.python.org/distribute/setuptools.html#declaring-dependencies
install_requires = [
    'numpy'
]
setup(
    name='ares',
    version=VERSION,
    description="Adaptive multi-scale sub-sampling for timeseries data",
    long_description=README,
    classifiers=[
        # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='timeseries subsampling plotting',
    author='Igor Gotlibovych',
    author_email='igor.gotlibovych@gmail.com',
    url='https://github.com/ig248/ares',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    entry_points={
      'console_scripts': []
    }
)
