from setuptools import find_packages, setup

setup(
    name="forge_sync",
    packages=find_packages(exclude=["forge_sync_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
