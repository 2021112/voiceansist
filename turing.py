# -*- coding: utf-8 -*-
import requests
import json

class Turing():
    def __init__(self, key='29ccde937cd544afbd45667b4be9805e', id='12345'):
        self.key = key
        self.id = id

    def getHtml(self, url):
        html = requests.get(url).text
        return html

    def textinfo(self, dict):
        return dict['text']

    def linkinfo(self, dict):
        return dict['text'] + '\n' + dict['url']

    def newinfo(self, dict):
        text = ''
        text = text + dict['text'] + '\n'
        for newdict in dict['list']:
            text = text + newdict['article'] + '\n'
            text = text + newdict['source'] + '\n'
            text = text + newdict['detailurl'] + '\n'
            text = text + '-----------------------\n'
        return text

    def cookinfo(self, dict):
        text = ''
        text = text + dict['text']
        cookdict = dict['list']
        text = text + cookdict[0]['name'] + '\n'
        text = text + cookdict[0]['icon'] + '\n'
        text = text + cookdict[0]['info'] + '\n'
        text = text + cookdict[0]['detailurl'] + '\n'
        text = text + '-----------------------\n'
        return text

    def anser(self, info):
        api = 'http://www.tuling123.com/openapi/api?key=' + \
            self.key + '&userid=' + self.id + '&info='
        request = api + info
        response = self.getHtml(request)
        dic_json = json.loads(response)
        code = int(dic_json['code'])
        if code == 100000:
            return self.textinfo(dic_json)
        elif code == 200000:
            return self.linkinfo(dic_json)
        elif code == 302000:
            return self.newinfo(dic_json)
        elif code == 308000:
            return self.cookinfo(dic_json)
