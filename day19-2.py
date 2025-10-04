import logging
logging.basicConfig(
    level = logging.DEBUG,
    filename = "app.log",
    filemode = "w",
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Program started")
for i in range(3):
    logging.debug(f"Loop index: {i}")
logging.warning("Something might be wrong")
logging.error("This is an error message")
logging.critical("Critical issue occurred!")
logging.info("Program finished")