import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="httpRequest",
    version="0.0.1",
    author="DARKora7",
    author_email="morgtdicks@gmail.com",
    description="will extract json data and write to textfile",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DARKora7/httpRequests.git",
    packages=setuptools.find_packages(),
    install_requires=[ 'used_functions', ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
