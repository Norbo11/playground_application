import sys

import requests
import random
import time
import logging


logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

BASE_PATH = 'http://localhost:{}/api/'

def main():
    logger.info('Starting requests simulator')
    sleep_time = int(sys.argv[1])
    port = sys.argv[2]
    endpoints = sys.argv[3:]

    reqs = 0
    while True:
        endpoint = random.choice(endpoints)
        endpoint = BASE_PATH.format(port) + endpoint

        logger.info(f'Sending request to {endpoint}')

        try:
            requests.get(endpoint)
        except:
            pass

        reqs += 1 
        time.sleep(sleep_time)

    logger.info(f'Sent {reqs} requests')
    
if __name__ == '__main__':
    main()
