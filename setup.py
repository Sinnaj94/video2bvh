import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='video2bvh',
    version='0.1',
    author='KevinLTT',
    description='Extract motion capturing data from RGB videos',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url='https://github.com/Sinnaj94/video2bvh',
    python_requires='>=3.6',
)