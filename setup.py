#!/usr/bin/env python
import io
import re
from setuptools import setup, find_packages
import sys

with io.open('./kanoodlegenius2d/__init__.py', encoding='utf8') as version_file:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")


with io.open('README.rst', encoding='utf8') as readme:
    long_description = readme.read()


setup(
    name='kanoodlegenius2d',
    version=version,
    description='A touchscreen version of the Kanoodle Genius puzzle game',
    long_description=long_description,
    author='Will Keeling',
    author_email='will@zifferent.com',
    license='MIT license',
    packages=find_packages(
        exclude=[
            'docs', 'tests',
            'windows', 'macOS', 'linux',
            'iOS', 'android',
            'django'
        ]
    ),
    include_package_data = True,
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT license',
    ],
    install_requires=[
    ],
    options={
        'app': {
            'formal_name': 'kanoodlegenius2d',
            'bundle': 'com.zifferent'
        },

        # Desktop/laptop deployments
        'macos': {
            'app_requires': [
            ]
        },
        'linux': {
            'app_requires': [
            ]
        },
        'windows': {
            'app_requires': [
            ]
        },

        # Mobile deployments
        'ios': {
            'app_requires': [
            ]
        },
        'android': {
            'app_requires': [
            ]
        },

        # Web deployments
        'django': {
            'app_requires': [
            ]
        },
    }
)
