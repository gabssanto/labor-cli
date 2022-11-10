#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Nov 09 13:43:12 2022
@author ccavalcante
"""

from labor.enums.api import LaborApiEnum
from labor.utils.web import WebUtil

class LoginService:

    def __init__(self):

        self.__web_util = WebUtil()

        self.__logged_user_key = 'user.auth' 

    def do_login(self, email, password):
        """
        Login the user and creates a session

        Parameters
        ----------
            email {str}
            password {str}

        Returns
        -------
            dict, int
        """

        body = {
                'email': email,
                'password': password
                }

        res = self.__web_util.do_request(
                LaborApiEnum.SIGN_IN,
                body=body,
                method='post'
                )

        return res.json(), res.status_code 

