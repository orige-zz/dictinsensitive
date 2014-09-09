from setuptools import setup

setup(
    name='DictInsensitive',
    version='0.1.0',
    license='MIT',

    author='Eduardo Orige',
    author_email='eduardo.orige@gmail.com',

    description='Python dictionaries with case insensitive keys',
    keywords=['dictionaries', 'dict', 'dictionary'],

    url='http://github.com/orige/dictinsensitive',
    download_url='http://github.com/orige/dictinsensitive/downloads',

    include_package_data=True,
    packages=['dictinsensitive'],
    zip_false=False,
    test_suite='dictinsensitive.tests',

    install_requires=['six>=1.4.1']
)
