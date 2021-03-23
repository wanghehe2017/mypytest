# -*- coding: utf-8 -*-
import requests
class HttpRequests(object):

    def __init__(self, url):
        self.url = url
        self.req = requests.session()
        # 自定义请求头，根据自身所在公司项目需求
        self.headers = {'Content-Type': 'application/json', 'User-Agent': 'Node midway-v2x Version/1.28.1'}

    # 封装get请求
    def get(self, url='', params='', data='', headers=None, cookies=None):
        response = self.req.get(url=url, params=params, data=data, headers=headers, cookies=cookies)
        return response

    # post请求
    def post(self, url='', params='', data='', headers=None, cookies=None):
        response = self.req.post(url=url, params=params, data=data, headers=headers, cookies=cookies)
        return response

    # put请求
    def put(self, url='', params='', data='', headers=None, cookies=None):
        response = self.req.put(url=url, params=params, data=data, headers=headers, cookies=cookies)
        return response

    # delete请求
    def delete(self, url='', params='', data='', headers=None, cookies=None):
        response = self.req.delete(url=url, params=params, data=data, headers=headers, cookies=cookies)
        return response
