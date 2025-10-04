import logging
import re

# Configure logging
logging.basicConfig(
    level = logging.DEBUG,
    filename = "app.log",
    filemode = "w",
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Program Started")

try:
    with open("sample.txt", "r", encoding = "utf-8") as f:
        text = f.read()
        logging.info(f"Read file successfully, length: {len(text)} characters")
except FileNotFoundError:
    logging.error("Sample.txt not found!")
    text = ""

words = re.findall(r"\b\w+\b", text.lower())
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1
    logging.debug(f"Word '{word}' count now: {freq[word]}")
    if freq[word] > 5:
        logging.warning(f"Word '{word}' occurs more than 5 times!")

logging.info(f"Found {len(freq)} unique words")

top10 = sorted(freq.items(), key = lambda x: x[1], reverse = True)[:10]
logging.info(f"Top 10 most frequent words: {top10}")

logging.info("Program finished")
