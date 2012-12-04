"""
Decorator for methods to cache return value
"""

import functools


class cached_method(object):

    def __init__(self, func):
        self.func = func
        self.result_cache = dict()
        self.method_cache = dict()

    def __call__(self, *args):
        evaluator = lambda: self.func(*args)
        return self.cache_get(self.result_cache, args, evaluator)

    def __get__(self, obj, objtype):
        proxy = lambda: self.__class__(functools.partial(self.func, obj))
        return self.cache_get(self.method_cache, obj, proxy)

    def cache_get(self, cache, key, func):
        try:
            return cache[key]
        except KeyError:
            result = cache[key] = func()
            return result

