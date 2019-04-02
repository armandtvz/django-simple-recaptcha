import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-simple-recaptcha',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='GPL-3.0',
    description='A Django package for Google reCAPTCHA v2. See README and docs for more.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/armandtvz/django-simple-recaptcha',
    author='Armandt van Zyl',
    author_email='armandtvz@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL-3.0',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'requests',
    ],
)
