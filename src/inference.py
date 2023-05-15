import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("inference")


def run_inference(_image: bytes) -> str:
    logger.info(f"Started running inference")
    time.sleep(2)
    logger.info("Finished running inference")
    return "🐶"
