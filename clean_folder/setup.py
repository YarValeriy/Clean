from setuptools import setup, find_namespace_packages

setup(
    name="clean",
    version="1.1.1",
    description="Folder cleaner",
    url="https://github.com/YarValeriy/Python-course/blob/main/clean.py",
    author="Valeriy",
    author_email="yar.valeriy@yahoo.com",
    license="MIT",
    packages=find_namespace_packages(),
    entry_points={"console_scripts": ["clean-folder = clean_folder.clean:sort_files"]},
)
