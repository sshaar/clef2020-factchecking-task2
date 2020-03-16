#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import logging
from logging import handlers
from colorlog import ColoredFormatter


def Logger():
    file_frmt = logging.Formatter(
        '[%(asctime)s ][%(levelname)-8s][%(message)s ]')
    stream_frmt = ColoredFormatter(
        '[%(asctime)s ][%(log_color)s%(levelname)-8s%(reset)s][%(log_color)s%(message)s%(reset)s ]')

    logger = logging.getLogger('Threshold')
    logger.setLevel(logging.DEBUG)

    # file handler
    fh = logging.FileHandler('RandomThreshold.log')

    # stream handler
    ch = logging.StreamHandler()

    ch.setFormatter(stream_frmt)
    fh.setFormatter(file_frmt)

    logger.addHandler(ch)
    logger.addHandler(fh)
    return logger


logger = Logger()
