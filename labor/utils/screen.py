#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on qui nov 10 09:30:32 2022
@author ccavalcante
"""
import os

import fortune
from .alert import AlertUtil

class Screen:
    """
    Used to manage the terminal screen
    """

    HEARTH_CHAR = "\u2764\uFE0F"

    @classmethod
    def clean(cls):
        """
        Clean the screen

        # Note: does not work in Windows machine yet
        """

        os.system('clear')

    @classmethod
    def show_banner(cls):
        """
        Cleans the terminal window and print the labor banner
        """
        cls.clean()

        f = open('./labor/banner.txt')

        hearth = AlertUtil.paint(cls.HEARTH_CHAR, 'red')

        novatics_label = '\033[1m' + 'Novatics' + '\033[0m'

        love_message = f"Made with {hearth} by {novatics_label}"

        print('\n\n', f.read(), '\n', love_message, '\n')

    @classmethod
    def goodbye_message(cls):

        print('\n\n')

        AlertUtil.warn(
                fortune.get_random_fortune('./fortune.txt')
               ) 

        print('\n')

