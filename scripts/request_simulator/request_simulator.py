import sys
import requests
import random
import time
import logging

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

    req_df = pd.DataFrame(columns=['endpoint', 'duration', 'status', 'response'])

    for i in range(total_requests):
        endpoints_dict = config['endpoints']
        endpoint = random.choice(list(endpoints_dict.keys()))

        logger.info(f'Sending request to {endpoint}')

        start_time = time.time()
        body = json.loads(endpoints_dict[endpoint]['json']) if 'json' in endpoints_dict[endpoint] else None
        response = requests.request(endpoints_dict[endpoint]['method'], config['base_path'] + '/' + endpoint, json=body)
        end_time = time.time()

        req_df.loc[i] = {'endpoint': endpoint,
                         'duration': end_time - start_time,
                         'status': response.status_code,
                         'response': response.json()['i'] if response.ok else ""
                         }

        time.sleep(config['sleep_time'])
        req_df.to_csv(results_filename)

    logger.info(f'Sent {total_requests} requests')


if __name__ == '__main__':
    main()
