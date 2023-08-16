# Logging means - You can add logs to the Failure, Information, Error
# Warning to the Users

import logging


def test_print_logs():
    LOGGER = logging.getLogger(__name__)

    # Intentional Logging to User
    LOGGER.info("This is information Logs")
    LOGGER.warning("This is Warning Logs")
    LOGGER.error("This is Error Logs")
    LOGGER.critical("This is Critical Logs")
