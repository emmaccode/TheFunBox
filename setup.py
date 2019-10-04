import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TheFunBox",
    version="0.0.1",
    author="Emmett Boudreau",
    author_email="emmett@emmettboudreau.com",
    description="A small stats and rescaling sample.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/emmettgb/TheFunBox",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
