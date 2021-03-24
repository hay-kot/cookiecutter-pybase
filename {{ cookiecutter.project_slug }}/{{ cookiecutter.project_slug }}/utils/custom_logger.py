import logging
from pathlib import Path

import coloredlogs
from {{cookiecutter.project_slug}}.core.settings import settings

LOGGER_LEVEL = "INFO"
CWD = Path(__file__).parent
LOGGER_FILE = settings.BASE_DIR.joinpath("{{ cookiecutter.project_slug }}.log")


logging.basicConfig(
    level=LOGGER_LEVEL,
    format="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    filename=LOGGER_FILE,
)
coloredlogs.install(
    level=LOGGER_LEVEL,
    fmt="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)

logger = logging.getLogger(__name__)


""" Logging Cheat Sheet
logger.debug("this is a debugging message")
logger.info("this is an informational message")
logger.warning("this is a warning message")
logger.error("this is an error message")
logger.critical("this is a critical message")
"""

if __name__ == "__main__":
    logger.debug("this is a debugging message")
    logger.info("this is an informational message")
    logger.warning("this is a warning message")
    logger.error("this is an error message")
    logger.critical("this is a critical message")
