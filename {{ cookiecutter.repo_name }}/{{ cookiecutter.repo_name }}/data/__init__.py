"""
Expose the API for the main functions in the data modules.
This makes it more convenient to call the data functions from the CLI
and adds a layer of abstraction.
"""

from {{ cookiecutter.repo_name }}.data.download_data import download_data
from {{ cookiecutter.repo_name }}.data.make_dataset import make_dataset
