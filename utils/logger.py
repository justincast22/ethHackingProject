import logging


def setup_logger():
    """Sets up basic logging."""

    logging.basicConfig(
        filename="enumeration.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    return logging.getLogger(__name__)