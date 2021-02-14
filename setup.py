from setuptools import setup

setup(
    name='spotify',
    packages=['spotify'],
    include_package_data=True,
    install_requires=[
        'flask',
        'requests'
    ],
)