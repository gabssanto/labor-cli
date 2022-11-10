#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on qui nov 10 09:29:56 2022
@author ccavalcante
"""

from labor.enums.api import LaborApiEnum
from labor.utils.web import WebUtil


class TasksService:
    """ Manage labor tasks """

    def __init__(self):

        self.__web_util = WebUtil()

    def _get_full_path(self, path):

        return LaborApiEnum.TASKS

    def get_opened_task(self):

        full_path = self._get_full_path(LaborApiEnum.OPENED)

        res = self.__web_util.do_request(
                full_path,
                method='get'
                )

        return res
