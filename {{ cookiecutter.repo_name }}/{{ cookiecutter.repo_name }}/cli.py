import click
import logging
import {{ cookiecutter.repo_name }}


class Config(object):
    def __init__(self):
        self.verbose = False
        self.logger = None


pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option("--verbose", "-v", is_flag=True, help="Print more logging messages.")
@pass_config
def cli(config, verbose):
    """Run commands from cfb_rankings_analysis module."""
    config.verbose = verbose
    config.logger = create_root_logger(verbose)

    config.logger.info("Start CLI program.")


@cli.command()
@pass_config
def download_data(config):
    """
    Download external data.
    Download external data into `data/external`.
    """
    config.logger.info("Download external data")

    {{ cookiecutter.repo_name }}.data.download_data.main()

    config.logger.info("External data download complete")


@cli.command()
@pass_config
def make_dataset(config):
    """
    Make an interim dataset.
    Transform data from `data/raw` and/or `data/external` into a dataset in `data/interim`.
    """
    config.logger.info("Make dataset")

    {{ cookiecutter.repo_name }}.data.make_dataset.main()

    config.logger.info("Dataset made")


@cli.command()
@pass_config
def process_dataset(config):
    """
    Make a final processed dataset.
    Transform data from `data/interim` into a final processed dataset in `data/processed`.
    """
    config.logger.info("Make final processed dataset")

    {{ cookiecutter.repo_name }}.data.process_dataset.main()

    config.logger.info("Final processed dataset made")


def create_root_logger(verbose):
    """
    Create a root logger
    """
    # create the logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # create a file handler
    file_handler = logging.FileHandler(".log")
    file_handler.setLevel(logging.DEBUG)

    # create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(set_handler_level(verbose))

    # create formatter and add to handlers
    formatter = logging.Formatter(
        "%(asctime)s :: %(name)s :: %(levelname)s :: %(message)s"
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


def set_handler_level(verbose):
    if verbose:
        return logging.DEBUG
    else:
        return logging.ERROR
