#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on qui nov 10 09:29:49 2022
@author ccavalcante
"""

from labor.services.tasks import TasksService
from labor.utils.alert import AlertUtil

class TasksController:
    """
    Controller used to manage tasks
    """

    def __init__(self):

        self.__service = TasksService()

    def opened_task(self):

        res = self.__service.get_opened_task()

        AlertUtil.print_json(res.json())
