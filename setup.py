from setuptools import setup

setup(
    name="data-process-framework",
    version="0.2.2",
    description="Framework for creating data processes.",
    url="",
    author="Steven Barnes",
    author_email="steven.barnes@swbdevelopment.com",
    packages=['dataprocess','dataprocess.abstractions','dataprocess.helpers','dataprocess.utilities'],
    install_requires=[
        # 'pandas>=1.4.2',
        # 'openpyxl>=3.0.7'
    ]
)