from pathlib import Path
from setuptools import setup, find_packages

setup(
    name="medicine",
    version="0.0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=Path("requirements.txt").open().readlines(),
    py_modules=["medicine.main"],
    entry_points={
        "console_scripts": [
            "medicine = medicine.main:run",
        ],
    },
)