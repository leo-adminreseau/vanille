from setuptools import setup, find_packages

setup(
    name='groupe2_package',  # Replace with your package name
    version='0.1',  # Initial version number
    packages=find_packages(),  # Automatically find and include all packages
    install_requires=['pandas'],  # List your package dependencies here
    author='groupe2',  # Replace with your name
    author_email='groupe2@gmail.com',  # Replace with your email
    description='Filter and join functionalities on csv files',
    long_description=open('README.md').read(),  # Reads the content of README.md
    long_description_content_type='text/markdown',  # Ensures correct rendering of Markdown
    url='https://github.com/nicolaselhayek/nicolas_package',  # Replace with your project's URL (optional)
    classifiers=[
        'Programming Language :: Python :: 3',  # Specify supported Python versions
        'License :: OSI Approved :: MIT License',  # Specify the license (you can choose different one)
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version required
)
