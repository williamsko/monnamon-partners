from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='monnamon-partners',
    version='0.0.1',
    author='Williams de SOUZA',
    author_email='williamsko89@gmail.com',
    description='Monnamon\'s partners api consumption',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/williamsko/monnamon-partners.git',
    packages=['monnamon'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'requests',
        'json',
        'cerberus',
    ],
)
