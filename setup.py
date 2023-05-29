from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pdf_parser',
    version='1.0.0',
    author='Nithin S Varrier',
    description='PDF Parser using Camelot',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/0x006e/pdf_parser',
    packages=find_packages(include=['pdf_parser', 'pdf_parser.*']),
    install_requires=[
        'camelot-py[cv]',
        'pandas'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
