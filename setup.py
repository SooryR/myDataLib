from setuptools import setup, find_packages

setup(
    name='myDataLib',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[                    # List of required dependencies
        'numpy',
        'pandas',
        'scipy',
        'statsmodels',
        'scikit-learn',
        'matplotlib',
        'seaborn',
      # Add other dependencies if needed
    ],
    author='Soory',
    author_email='soory.ranga@gmail.com',
    description='A Python library for data cleaning and analysis',
    #long_description=open('README.md').read(),  # Read from README.md
    #long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my_data_lib', # Replace with your GitHub repo
    license='MIT',                            # Your License (e.g. MIT)
    classifiers=[
        "Programming Language :: Python :: 3", #add as necessary from https://pypi.org/classifiers/
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',  # Specify minimum Python version
)