{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter or RMarkdown notebooks.
    |                         Naming convention is a number (for ordering), the creator's initials,
    |                         and a short `-` delimited description,
    |                         e.g. `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── {{ cookecutter.repo_name }}   <- Source code for python package used in this project.
    │   ├── __init__.py    <- Makes {{ cookecutter.repo_name }} a Python module
    │   ├── cli.py         <- Defines a CLI for the package. 
    │   │                     Access from the command line with {{ cookiecutter.repo_name.replace("_", "-") }}
    │   │
    │   ├── data           <- Scripts to download, generate, and/or process data.
    │   │   └── __init__.py         <- Exposes the API for the data module.
    │   │   └── download_data.py    <- Download data from external sources.
    │   │   └── make_dataset.py     <- Make interim dataset from raw and/or external data.
    │   │   └── process_dataset.py  <- Process interim dataset into a final processed dataset.
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

--------

<p><small>Project based on the <a target="_blank" href="https://github.com/trev-f/cookiecutter-data-science">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
