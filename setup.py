from setuptools import setup, find_packages

setup(
    name="sales_analysis",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas==2.2.1",
        "numpy==1.26.4",
        "matplotlib==3.8.4",
        "seaborn==0.12.2",
        "scipy==1.13.0",
        "plotly==5.22.0",
    ],
    entry_points={
        "console_scripts": [
            "sales-analysis=main:main",
        ],
    },
    author="Artem Fleisher",
    description="Data analysis project based on Online Retail II dataset",
    python_requires=">=3.9",
)
