import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='video2bvh',
    version='0.3',
    author='Jannis Jahr (MIT License KevinLTT)',
    description='Extract motion capturing data from RGB videos',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=["easydict",
                      "numpy",
                      "torch",
                      "h5py",
                      "matplotlib",
                      "PyYAML"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url='https://github.com/Sinnaj94/video2bvh',
    python_requires='>=3.6',
)
