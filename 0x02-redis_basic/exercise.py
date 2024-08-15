#!/usr/bin/env python3
""" A module to learn Redis Datastorage
"""
import uuid
import redis
from typing import Any, Callable, Union

class Cache:
    """ Class to store data in Redis """
    def __init__(self) -> None:
        """ init file """
        self._redis = redis.Redis()
        self._redis.flushdb(True)


    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store data in redis storage and return key
        """
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key
