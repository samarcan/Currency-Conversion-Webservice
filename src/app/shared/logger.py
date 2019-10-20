import datetime
import logging
import os
from typing import Dict

import settings


class SingletonServiceMetaclass(type):
    _instances: Dict = {}

    def __call__(cls, serviceName, *args, **kwargs):
        if serviceName not in cls._instances:
            cls._instances[serviceName] = super(
                SingletonServiceMetaclass, cls
            ).__call__(serviceName, *args, **kwargs)
        return cls._instances[serviceName]


class AppLogger(object, metaclass=SingletonServiceMetaclass):
    def __init__(self, serviceName):
        self._serviceName = serviceName
        self._baseLevel = settings.LOGGER_LEVEL
        self._logger = logging.getLogger(self._serviceName)
        self.__setLevel()
        self.__setStreamHandler(self.__getFormatter())

    def __getFormatter(self):
        return logging.Formatter(
            "%(asctime)s \t [%(levelname)s | " "%(filename)s:%(lineno)s] > %(message)s"
        )

    def __setStreamHandler(self, formatter):
        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(formatter)
        self._logger.addHandler(streamHandler)

    def __setLevel(self):
        if self._baseLevel == "INFO":
            self._logger.setLevel(logging.INFO)
        elif self._baseLevel == "WARNING":
            self._logger.setLevel(logging.WARNING)
        elif self._baseLevel == "ERROR":
            self._logger.setLevel(logging.ERROR)
        elif self._baseLevel == "CRITICAL":
            self._logger.setLevel(logging.CRITICAL)
        else:
            self._logger.setLevel(logging.DEBUG)

    def get_logger(self):
        return self._logger


def getAppLogger(serviceName):
    return AppLogger.__call__(serviceName).get_logger()
