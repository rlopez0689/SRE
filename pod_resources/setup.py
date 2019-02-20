from setuptools import setup, find_packages

setup(
    name='pod_resources',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    scripts=['bin/pod_resources']
)
