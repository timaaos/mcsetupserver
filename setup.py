import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="mc-server-setup",
    version="1.0.0",
    description="Setup minecraft servers with easy!",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/timaaos/mcserversetup",
    author="Timaaos",
    author_email="whybrawlmail@gmail.com",
    license="No license",
    classifiers=[
        "License :: No License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["mcserversetup"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "mc_server_setup=reader.setupserver:main",
        ]
    },
)