#day22_logging_examples.py
import logging
#Configure Logging
logging.basicConfig(
    level = logging.DEBUG,
    filename = "app.log",
    filemode = "w",
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

#output to console
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s - %(message)s')
console.setFormatter(formatter)
logging.getLogger().addHandler(console)

#Two Sum
def two_sum(nums, target):
    logging.info("Running Two Sum")
    lookup = {}
    for i, num in enumerate(nums):
        complement = target - num
        logging.debug(f"Index {i}: num = {num}, complement = {complement}")
        if complement in lookup:
            logging.info(f"Found pair: {complement} + {num} = {target}")
            return [lookup[complement], i]
        lookup[num] = i
    logging.warning("No pair found")
    return []

nums = [2, 7, 11, 15]
target = 9
print("Two Sum result:", two_sum(nums, target))


#Contain Duplicate
def contains_duplicate(nums):
    logging.info(f"Running Contains Duplicate")
    seen = set()
    for num in nums:
        logging.debug(f"Checking {num}")
        if num in seen:
            logging.info(f"Duplicate found: {num}")
            return True
        seen.add(num)
    logging.info(f"No duplicate found")
    return False

nums2 = [1, 2, 3, 1]
print("Contains Duplicate:", contains_duplicate(nums2))

#Valid Anagram
def is_anagram(s, t):
    logging.info(f"Running Valid Anagram")
    if len(s) != len(t):
        logging.warning(f"Length mismathc")
        return False
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
        logging.debug(f"Count for {char}: {freq[char]}")
    for char in t:
        if char not in freq or freq[char] == 0:
            logging.warning(f"Char {char} mismatch")
            return False
        freq[char] -= 1
        logging.debug(f"Decreased count for {char}: {freq[char]}")
    logging.info(f"Strings are anagrams")
    return True

s = "anagram"
t = "nagaram"
print("Valid Anagram:", is_anagram(s, t))




