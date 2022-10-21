import click
import logging


def make_dataset():
    """
    Main logic for the subcommand make-dataset
    """
    logger = logging.getLogger(__name__)

    logger.info("Start the main function for make dataset")

    click.echo("Make dataset!")

    logger.info("End of the main function for make dataset")


if __name__ == "__main__":
    make_dataset()
