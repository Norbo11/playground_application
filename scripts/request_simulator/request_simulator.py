import sys
import requests
import random
import time
import logging
import itertools
import yaml
import json
from yaml import CLoader
import pandas as pd

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def main():
    logger.info('Starting requests simulator')

    config_filename = sys.argv[1]
    results_filename = sys.argv[2]
    total_requests = int(sys.argv[3])

    with open(config_filename, 'r') as config_file:
        config = yaml.load(config_file, Loader=CLoader)

    req_df = pd.DataFrame(columns=['endpoint', 'duration', 'status', 'controller_time', 'request_time'])
    endpoints = config['endpoints']

    for i, endpoint_dict in enumerate(itertools.cycle(endpoints)):
        if i == total_requests:
            break

        endpoint = endpoint_dict['endpoint']
        logger.info(f'Sending request to {endpoint}')

        try:
            start_time = time.time()
            body = json.loads(endpoint_dict['json']) if 'json' in endpoint_dict else None
            params = json.loads(endpoint_dict['params']) if 'params' in endpoint_dict else None
            response = requests.request(endpoint_dict['method'], config['base_path'] + '/' + endpoint, json=body, params=params)
            end_time = time.time()
        except Exception as e:
            logger.warning(f"Exception: {e}")

        time.sleep(config['sleep_time'])

    logger.info(f'Sent {total_requests} requests')


if __name__ == '__main__':
    main()
