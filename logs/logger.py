import logging


logger = logging.getLogger("api_logger")
logger.setLevel(logging.INFO)
logger_handler = logging.FileHandler("../logs/api.log")
logger_formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
logger_handler.setFormatter(logger_formatter)
logger.addHandler(logger_handler)

