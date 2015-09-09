#!/usr/bin/env/python
from setuptools import setup

setup(
    name='ckanext-nrgickantheme',
    version='0.1',
    description='',
    license='AGPL3',
    author='',
    author_email='',
    url='',
    namespace_packages=['ckanext'],
    packages=['ckanext.nrgickantheme'],
    zip_safe=False,
    entry_points = """
        [ckan.plugins]
        nrgickan_theme = ckanext.nrgickantheme.plugins:CustomTheme
    """
)
