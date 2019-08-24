import re

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    name="quicktext",
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    # install_requires=requirements,
    # setup_requires=setup_requirements,
    # extras_require=dev_requirements,
    # tests_require=test_requirements,
    python_requires=">=3.6",
    # test_suite="tests",
    description="",
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords="smartreply, deep learning, machine learning",
    url="https://github.com/verloop/smartreply",
    author="Nirant Kasliwal",
    author_email="nirant@verloop.io",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    zip_safe=False,
)