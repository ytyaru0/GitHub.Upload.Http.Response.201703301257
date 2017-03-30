#!python3
#encoding:utf-8
import json
import time
from urllib.parse import urlparse
import re
import web.http.Response
class Response(web.http.Response.Response):
    def __init__(self):
        super().__init__()
        self.re_content_type_raw = re.compile('application/vnd.github.*.raw')
#        self.re_charset = re.compile(r'charset=', re.IGNORECASE)
#        self.__mime_type = None
#        self.__char_set = None
    """
    HTTP応答データを返す
    @param {requests.response} 応答データを作成するため。
    @return {?} Content-Typeなどにより任意のデータ型を返す。
    """
    def Get(self, r, sleep_time=2, is_show=True):
        res = super.Get(r, sleep_time, is_show)
        if 'json' == self.Headers.ContentType.suffix:
            return r.json()
        elif self.re_content_type_raw.match(self.Headers.ContentType.mime_type):
            return r.content
        else:
            return res
        """
        self.__SplitContentType(r)
        if None is self.__mime_type:
            return r.text
        elif 'application/json' == self.__mime_type:
            return r.json()
        elif self.re_content_type_raw.match(self.__mime_type):
            return r.content
        else:
            raise Exception('対象外のContent-Typeです。: ' + self.__mime_type)
#    def Get(self, r, res_type=None, success_code=None, sleep_time=2, is_show=True):
        if is_show:
            print("HTTP Status Code: {0}".format(r.status_code))
            print(r.text)
        time.sleep(sleep_time)
        r.raise_for_status()
#        if None is not success_code:
#            if (success_code != r.status_code):
#                raise Exception('HTTP Error: {0}'.format(r.status_code))
#                return None
        
        self.__SplitContentType(r)
        if None is self.__mime_type:
            return r.text
        elif 'application/json' == self.__mime_type:
            return r.json()
        elif self.re_content_type_raw.match(self.__mime_type):
            return r.content
        else:
            raise Exception('対象外のContent-Typeです。: ' + self.__mime_type)
#        if None is res_type or 'text' == res_type.lower():
#            return r.text
#        elif 'json' == res_type.lower():
#            return r.json()
#        elif 'binary' == res_type.lower():
#            return r.content
#        else:
#            raise Exception("指定されたres_type {0} は対象外です。".format(res_type))
        """
