#!/usr/bin/python
import setuptools

setuptools.setup(name='bell_parallel',
    version='0.0.1',
    description='Parallel execution utils',
    author='Fabian Bell',
    author_email='fabianx.bell@gmail.com',
    url='https://github.com/FabianBell/Packages',
    license='MIT',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_required='>=3.8'
    )
