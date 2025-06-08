import os
from setuptools import setup, find_packages

setup(
    name='pubstyle',
    version='1.0.0', # Incrementing version slightly due to new features/renaming
    description='Custom Matplotlib styles for publication-quality plots.',
    author='Your Name',  # Replace with your name
    author_email='your.email@example.com',  # Replace with your email
    packages=find_packages(where='.'), # Explicitly look in current directory
    package_dir={'': '.'}, # Tell setuptools that packages are in the current directory
    install_requires=[
        'matplotlib>=3.3', # Specify a reasonable minimum version
    ],
    entry_points={
        'console_scripts': [
            'pubstyle-cli=pubstyle.cli:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License', # Assuming MIT, can be changed
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Scientific/Engineering :: Visualization',
        'Framework :: Matplotlib',
    ],
    python_requires='>=3.7',
    long_description=open('README.md').read() if os.path.exists('README.md') else '',
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/pubstyle', # Replace with your repo URL
)
