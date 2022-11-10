#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on qui nov 10 10:03:29 2022
@author ccavalcante
"""

from .config import Configuration

class SessionUtil:
    """ Adds a class description here """

    __instance = None

    def __init__(self):

        if SessionUtil.__instance is not None:
            raise Exception(
                    "this is a singleton, use get_instance instead"
                    )

        self.__config = Configuration.get_instance()
        self.__logged_user_key = 'user.auth' 

        SessionUtil.__instance = self

    @staticmethod
    def get_instance():
        
        if SessionUtil.__instance is None:
            SessionUtil()

        return SessionUtil.__instance

    @property
    def logged_user(self) -> dict:

        return self.__config.get(self.__logged_user_key)

    @logged_user.setter
    def logged_user(self, logged_user: dict):

        self.__config.put(
                self.__logged_user_key,
                logged_user
                )

        self.__config.write()

