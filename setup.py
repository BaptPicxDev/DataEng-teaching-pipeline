# Imports
from setuptools import find_packages, setup


# Setup
setup(
    name="bpd_data_engineering_course",
    version="0.1.0",
    python_requires="==3.12.*",
    install_requires=[
        "wheel==0.44.0",
        "numpy==1.26.4",
        "pandas==2.1.2",
        "kaggle",
        "lxml",
    ],
)
