from setuptools import setup, find_packages

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='chathuri madhushika',
    author_email='chathuri.uom@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
) 