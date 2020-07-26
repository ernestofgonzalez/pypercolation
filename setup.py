import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pypercolation",
    version="0.0.1",
    author="Ernesto González",
    author_email="ernestogonzalezz@yahoo.com",
    description="Python percolation package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ErnestoFGonzalez/pypercolation",
    packages=['pypercolation'],
    install_requires=['numpy',
                      'networkx',
                      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
    ],
    python_requires='>=3.6',
)
