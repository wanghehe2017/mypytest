# -*- coding: utf-8 -*-
import os
import sys

import json
from venv import logger

from fixture.v2x_fixture import *
from config.url_conf import URLConf

project_root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(project_root)


class TestV2x:
    @pytest.mark.smoke
    def test_001_queryArea(self, http, get_token):
        """查询区域"""
        playload = {"cmd": "queryArea", "csrfToken": get_token, "params": {"cityId": "320200"}}
        response = http.post(url=URLConf.TEST_URL.value, data=json.dumps(playload), headers=URLConf.HEADERS.value)
        resultNote = response.json()
        assert resultNote.get('resultNote'), 'success'
        logger.info('查询区域成功')

    def test_002_queryYearlyCheckCount(self, http, get_token):
        """查询年检总数"""
        playload = {"cmd": "queryYearlyCheckCount", "Token": get_token, "params": {}}
        response = http.post(url=URLConf.TEST_URL.value, data=json.dumps(playload), headers=URLConf.HEADERS.value)
        resultNote = response.json()
        assert resultNote.get('resultNote'), 'SUCCESS'
        logger.info('查询年检成功')

    def test_003_queryTrafficEvent(self, http, get_token):
        """查询交通事件"""
        playload = {"cmd": "queryTrafficEvent", "Token": get_token, "params": {}}
        response = http.post(url=URLConf.TEST_URL.value, data=json.dumps(playload), headers=URLConf.HEADERS.value)
        resultNote = response.json()
        assert resultNote.get('resultNote'), 'Success'
        logger.info('查询交通事件成功')

    def test_004_queryRsuCount(self, http, get_token):
        """查询rsu总数"""
        playload = {"cmd": "queryRsuCount", "Token": get_token, "params": {}}
        response = http.post(url=URLConf.TEST_URL.value, data=json.dumps(playload), headers=URLConf.HEADERS.value)
        resultNote = response.json()
        assert resultNote.get('resultNote'), '查询路测设备数量成功！'
        # text = response.text
        # print(text)
        logger.info('查询路侧设备成功')

    # 简单的数据驱动
    @pytest.mark.parametrize('deviceid', ['0086860703231572', '0086337601270714', '0086822412608154'])
    def test_005_queryDeviceDetail(self, http, get_token, deviceid):
        """查询设备详情"""
        playload = {"cmd": "queryDeviceDetail", "params": {"deviceId": deviceid}, "Token": get_token}
        response = http.post(url=URLConf.TEST_URL.value, data=json.dumps(playload), headers=URLConf.HEADERS.value)
        resultNote = response.json()
        assert resultNote.get('resultNote'), '查询终端信息成功！'
        logger.info('查询终端信息成功！')


if __name__ == '__main__':
    pytest.main(['-s', '-v', ])