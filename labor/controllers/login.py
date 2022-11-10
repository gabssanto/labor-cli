#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Nov 09 13:36:02 2022
@author ccavalcante
"""
import os

import click

from labor.services.login import LoginService 
from labor.utils.alert import AlertUtil
from labor.utils.screen import Screen

class LoginController:

    def __init__(self):

        self.__service = LoginService()

    def sign_in(self):

        Screen.show_banner()

        email = click.prompt(AlertUtil.paint('Enter your email', 'cyan'), type=str)
        password = click.prompt(
                AlertUtil.paint('Enter your password', 'cyan'), 
                type=str,
                hide_input=True)

        body, status_code = self.__service.do_login(email, password)

        if status_code != 200:

            errors = " ".join(body['errors'])

            AlertUtil.error(errors)

            return

        user_name = AlertUtil.paint(body['data']['name'], 'green')

        message = f'Seja bem-vindo {user_name}'

        AlertUtil.simple_print("\n\n" + message)
