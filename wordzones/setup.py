from pathlib import Path

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

reqs = Path("requirements.txt").resolve()
assert reqs.exists()

with open(reqs, "r") as f:
    requirements = f.readlines()

setup(
    name="wordzones",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    # setup_requires=setup_requirements,
    # tests_require=test_requirements,
    python_requires=">=3.6",
    test_suite="tests",
    description="Word Clouds, But Better",
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords="machine learning for whatsapp choice",
    url="https://github.com/NirantK/wordzones",
    author="Nirant Kasliwal",
    author_email="wordzones@nirantk.com",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
    ],
    zip_safe=False,
)