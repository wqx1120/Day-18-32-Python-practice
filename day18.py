
import logging
logging.basicConfig(
    level = logging.INFO,
    filename = "app.log",
    filemode = "w",
    format = "%(asctime)s - %(levelname)s -%(message)s"
)

logging.info("Program started")

try:
    with open("sample.txt", "r", encoding = "utf-8") as f:
        text = f.read()
        logging.info(f"Read file successfully, length: {len(text)} characters")
except FileNotFoundError:
    logging.error("sample.txt not found!")

words = text.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

logging.info(f"Found {len(freq)} unique words")
logging.info("Program finished")