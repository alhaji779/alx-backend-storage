#!/usr/bin/env python3
""" A module to learn Redis Datastorage
"""
import uuid
import redis
from typing import Any, Callable, Union
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Counts number of cache class"""
    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        """ invoker function """
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return invoker


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


    def get(self, key: str, fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        """ Retrive value from redis """
        data = self._redis.get(key)
        return fn(data) if fn is not None else data


    def get_str(self, key: str) -> str:
        """ retrieve a string """
        return self.get(key, lambda x: x.decode('utf-8'))


    def get_int(self, key: str) -> int:
        """ retrieves an interger from redis"""
        return self.get(key, lambda x: int(x))
