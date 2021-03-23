# -*- coding: utf-8 -*-
import pytest
from common.http_requests import HttpRequests
from config.url_conf import URLConf


@pytest.fixture(scope='function', autouse=True)
def http():
    url = URLConf.TEST_URL.value
    http = HttpRequests(url)
    return http


@pytest.fixture(scope='function', autouse=True)
def get_token(http):
    headers = {'Content-Type': 'application/json', 'User-Agent': 'Node midway-v2x Version/1.28.1'}
    response = http.post(url=URLConf.TEST_URL.value,
                         data='{"cmd":"signin","params":{"userName":"smarttest","password":"72be4b7f62832c516b85fb26de59df53"}}',
                         headers=headers)
    token = response.json()['detail']['token']
    return token