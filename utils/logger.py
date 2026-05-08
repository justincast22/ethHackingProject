import logging
from pathlib import Path


def setup_logger(log_file="logs/enumerator.log"):
    """
    Sets up application logging.
    """

    log_path = Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(
        logging.Formatter("%(levelname)s | %(message)s")
    )

    logging.getLogger().addHandler(console)

    return logging.getLogger()