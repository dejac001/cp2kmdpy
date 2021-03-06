import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cp2kmdpy", # Replace with your own username
    version="0.0.1",
    author="Ramanish Singh",
    author_email="singh891@umn.edu",
    description='A Python input/output interface to CP2K, developed as part of the MoSDeF simulation suite.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ramanishsingh/cp2kmdpy',
    packages=setuptools.find_packages(),

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
