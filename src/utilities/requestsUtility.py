import json

from src.configs.hosts_config import API_HOSTS

import os
import requests
from requests_oauthlib import OAuth1
import logging as logger


class RequestsUtility(object):

    def __init__(self):
        self.status_code = None
        self.env = os.environ.get('ENV', 'dev')
        self.base_url = API_HOSTS[self.env]
        self.sub_url = API_HOSTS[os.environ.get('ENV', 'dev')]
        self.auth = OAuth1("", "")

    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}
        url = self.sub_url + endpoint
        rs_api = requests.post(url, data=json.dumps(payload), headers=headers)
        self.status_code = rs_api.status_code
        assert self.status_code == int(
            expected_status_code), f'Expected Status Code {expected_status_code} but actual one is {self.status_code}'
        logger.debug(f"API response : {rs_api.json()}")
        return rs_api.json()

    def get(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}
        url = self.sub_url + endpoint
        rs_api = requests.get(url, data=json.dumps(payload), headers=headers)
        return rs_api

    def delete(self, endpoint, url=None, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}
        url = self.sub_url + endpoint
        rs_api = requests.delete(url, data=json.dumps(payload), headers=headers)
        self.status_code = rs_api.status_code
        assert self.status_code == int(
            expected_status_code), f'Expected Status Code {expected_status_code} but actual one is {self.status_code}'
        logger.debug(f"API response : {rs_api.json()}")
        return rs_api.json()

    def put(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}
        url = self.sub_url + endpoint
        rs_api = requests.put(url, data=json.dumps(payload), headers=headers)
        self.status_code = rs_api.status_code
        assert self.status_code == int(
            expected_status_code), f'Expected Status Code {expected_status_code} but actual one is {self.status_code}'
        logger.debug(f"API response : {rs_api.json()}")
        return rs_api.json()
