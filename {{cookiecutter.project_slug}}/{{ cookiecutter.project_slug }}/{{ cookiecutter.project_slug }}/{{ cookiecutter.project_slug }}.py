from pathlib import Path

from utils.custom_logger import logger

CWD = Path(__file__).parent

if __name__ == "__main__":
    logger.debug("this is a debugging message")
    logger.info("this is an informational message")
    logger.warning("this is a warning message")
    logger.error("this is an error message")
    logger.critical("this is a critical message")
