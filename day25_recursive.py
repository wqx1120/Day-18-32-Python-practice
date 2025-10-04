import logging
logging.basicConfig(
    level = logging.DEBUG,
    filename = "day25.log",
    filemode = "w",
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter("%(levelname)s - %(message)s")
console.setFormatter(formatter)
logging.getLogger().addHandler(console)



def fibonacci(n):
    logging.debug(f"fibonacci({n}) called")
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
        logging.debug(f"fibonacci({n}) = {result}")
        return result
    
def factorial(n):
    logging.debug(f"factorial({n}) called")
    if n < 0:
        raise ValueError("Negative input are not allowed")
    elif n == 0 or n == 1:
        return 1
    else:
        result = n * factorial(n - 1)
        logging.debug(f"factorial({n}) = {result}")
        return result
    
def print_pyramid(n):
    logging.debug(f"print_pyramid({n}) called")
    if n <= 0:
        return
    print('*' * n)
    print_pyramid(n - 1)

logging.info("Starting Day 25 Recursive Exercises")

fib_n = 10
fact_n = 5
pyramid_n = 4

logging.info(f"Fibonacci {fib_n}: {fibonacci(fib_n)}")
logging.info(f"Factorial {fact_n}: {factorial(fact_n)}")
print("Pyramid:")
print_pyramid(pyramid_n)

logging.info("Day 25 Exercises Finished")

