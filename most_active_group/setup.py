from setuptools import setup, find_packages

setup(
    name='most_active_group',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    scripts=['bin/most_active_group']
)
