#!/usr/bin/env python3
""" method to show all documents"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """ this method list all doc
    of a mongo collection
    """
    return [doc for doc in mongo_collection.find()]
