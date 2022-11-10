#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on qui nov 10 10:01:11 2022
@author ccavalcante
"""


import httpx
from labor.enums.api import LaborApiEnum
from .session import SessionUtil

class WebUtil:
    """
    Send requests
    """

    def __init__(self):

        self.session = SessionUtil.get_instance()

    def __update_header_interceptor(self, headers):

        headers = {
            'access-token': headers['access-token'],
            'client': headers['client'],
            'expiry': headers['expiry'],
            'uid': headers['uid'],
            'token-type': headers['token-type']
        }

        self.session.logged_user = headers

        return self

    def do_request(self,
                     url_path, 
                     body={},
                     method='get', 
                     intercept=True):

        headers = self.session.logged_user

        url = LaborApiEnum.BASE_URL + url_path 
        response = getattr(httpx, method)(
                url,
                #json=body,
                headers=headers
                )

        if intercept and response.status_code == 200:
            self.__update_header_interceptor(response.headers)

        return response



