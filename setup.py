import os
from setuptools import setup


# borrowed from Numpy https://github.com/numpy/numpy-stubs/blob/master/setup.py
def find_stubs(package):
    stubs = []
    for root, dirs, files in os.walk(package):
        for file in files:
            path = os.path.join(root, file).replace(package + os.sep, '', 1)
            stubs.append(path)
    return {package: stubs}


setup(
    name="pika-stubs",
    url="https://github.com/5uper5hoot/pika-stubs",
    author="Peter Schutt",
    author_email="peter@topsport.com.au",
    version="0.1",
    package_data=find_stubs("pika-stubs"),
    packages=["pika-stubs"],
)
