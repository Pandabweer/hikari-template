import logging
import time


def func(hi: str) -> str:
    return hi


while True:
    time.sleep(1)
    logging.warning("Hello World!")
